from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import Article, Categorie, Commentaire, Cours, Chapitre
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


# Vues d'authentification
def user_login(request):
    """Vue pour la connexion des utilisateurs"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenue {user.username} !')
                next_url = request.GET.get('next', 'blog:liste_articles')
                return redirect(next_url)
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')
    
    return render(request, 'blog/auth/login.html')


def user_signup(request):
    """Vue pour l'inscription des utilisateurs"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé avec succès pour {username} ! Vous pouvez maintenant vous connecter.')
            return redirect('blog:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.title()}: {error}')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'blog/auth/signup.html', context)


def user_logout(request):
    """Vue pour la déconnexion des utilisateurs"""
    username = request.user.username if request.user.is_authenticated else None
    logout(request)
    if username:
        messages.success(request, f'À bientôt {username} !')
    return redirect('blog:liste_articles')


# Vues pour les cours
def liste_cours(request):
    """Vue pour afficher la liste des cours disponibles"""
    cours_list = Cours.objects.filter(actif=True).order_by('ordre', 'titre')
    
    # Récupération des catégories pour le menu
    categories = Categorie.objects.all()
    
    context = {
        'cours_list': cours_list,
        'categories': categories,
    }
    return render(request, 'blog/cours/liste_cours.html', context)


def detail_cours(request, slug):
    """Vue pour afficher le détail d'un cours avec ses chapitres"""
    cours = get_object_or_404(Cours, slug=slug, actif=True)
    chapitres = cours.chapitres.all().order_by('ordre')
    
    context = {
        'cours': cours,
        'chapitres': chapitres,
    }
    return render(request, 'blog/cours/detail_cours.html', context)


def detail_chapitre(request, cours_slug, chapitre_slug):
    """Vue pour afficher le détail d'un chapitre"""
    cours = get_object_or_404(Cours, slug=cours_slug, actif=True)
    chapitre = get_object_or_404(Chapitre, cours=cours, slug=chapitre_slug)
    
    # Navigation entre chapitres
    chapitre_precedent = chapitre.get_chapitre_precedent()
    chapitre_suivant = chapitre.get_chapitre_suivant()
    
    # Tous les chapitres pour la navigation latérale
    tous_chapitres = cours.chapitres.all().order_by('ordre')
    
    context = {
        'cours': cours,
        'chapitre': chapitre,
        'chapitre_precedent': chapitre_precedent,
        'chapitre_suivant': chapitre_suivant,
        'tous_chapitres': tous_chapitres,
    }
    return render(request, 'blog/cours/detail_chapitre.html', context)