from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Page d'accueil du blog - liste des articles
    path('', views.liste_articles, name='liste_articles'),
    
    # Détail d'un article
    path('article/<slug:slug>/', views.detail_article, name='article_detail'),
    
    # Articles par catégorie
    path('categorie/<int:categorie_id>/', views.articles_par_categorie, name='articles_par_categorie'),
    
    # Ajouter un commentaire (pour AJAX si besoin)
    path('article/<slug:slug>/commentaire/', views.ajouter_commentaire, name='ajouter_commentaire'),
]