from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Article, Categorie, Commentaire
from .forms import CommentaireForm


def liste_articles(request):
    """Vue pour afficher la liste des articles publiés"""
    articles_list = Article.objects.filter(statut='published').select_related('categorie', 'auteur')
    
    # Filtrage par catégorie
    categorie_id = request.GET.get('categorie')
    if categorie_id:
        articles_list = articles_list.filter(categorie_id=categorie_id)
    
    # Recherche
    query = request.GET.get('q')
    if query:
        articles_list = articles_list.filter(
            Q(titre__icontains=query) | Q(contenu__icontains=query) | Q(extrait__icontains=query)
        )
    
    # Pagination
    paginator = Paginator(articles_list, 5)  # 5 articles par page
    page = request.GET.get('page')
    
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    # Récupération des catégories pour le menu
    categories = Categorie.objects.all()
    
    context = {
        'articles': articles,
        'categories': categories,
        'query': query,
        'categorie_selectionnee': categorie_id,
    }
    return render(request, 'blog/liste_articles.html', context)


def detail_article(request, slug):
    """Vue pour afficher le détail d'un article"""
    article = get_object_or_404(Article, slug=slug, statut='published')
    
    # Incrémenter les vues
    article.incrementer_vues()
    
    # Récupérer les commentaires actifs
    commentaires = article.commentaires.filter(actif=True).select_related('auteur')
    
    # Formulaire de commentaire
    if request.method == 'POST':
        if request.user.is_authenticated:
            commentaire_form = CommentaireForm(data=request.POST)
            if commentaire_form.is_valid():
                nouveau_commentaire = commentaire_form.save(commit=False)
                nouveau_commentaire.article = article
                nouveau_commentaire.auteur = request.user
                nouveau_commentaire.save()
                messages.success(request, 'Votre commentaire a été ajouté avec succès!')
                return redirect('blog:article_detail', slug=slug)
        else:
            messages.error(request, 'Vous devez être connecté pour commenter.')
            return redirect('blog:article_detail', slug=slug)
    else:
        commentaire_form = CommentaireForm()
    
    # Articles similaires (même catégorie)
    articles_similaires = Article.objects.filter(
        categorie=article.categorie,
        statut='published'
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'commentaires': commentaires,
        'commentaire_form': commentaire_form,
        'articles_similaires': articles_similaires,
    }
    return render(request, 'blog/detail_article.html', context)


def articles_par_categorie(request, categorie_id):
    """Vue pour afficher les articles d'une catégorie spécifique"""
    categorie = get_object_or_404(Categorie, id=categorie_id)
    articles_list = Article.objects.filter(
        categorie=categorie,
        statut='published'
    ).select_related('auteur')
    
    # Pagination
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page')
    
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    # Récupération de toutes les catégories pour le menu
    categories = Categorie.objects.all()
    
    context = {
        'articles': articles,
        'categorie': categorie,
        'categories': categories,
    }
    return render(request, 'blog/articles_par_categorie.html', context)


@login_required
def ajouter_commentaire(request, slug):
    """Vue pour ajouter un commentaire (AJAX ou redirection)"""
    article = get_object_or_404(Article, slug=slug, statut='published')
    
    if request.method == 'POST':
        commentaire_form = CommentaireForm(data=request.POST)
        if commentaire_form.is_valid():
            nouveau_commentaire = commentaire_form.save(commit=False)
            nouveau_commentaire.article = article
            nouveau_commentaire.auteur = request.user
            nouveau_commentaire.save()
            messages.success(request, 'Votre commentaire a été ajouté avec succès!')
        else:
            messages.error(request, 'Erreur dans le formulaire de commentaire.')
    
    return redirect('blog:article_detail', slug=slug)