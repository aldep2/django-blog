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
    
    # URLs d'authentification
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    
    # URLs des cours
    path('cours/', views.liste_cours, name='liste_cours'),
    path('cours/<slug:slug>/', views.detail_cours, name='detail_cours'),
    path('cours/<slug:cours_slug>/<slug:chapitre_slug>/', views.detail_chapitre, name='detail_chapitre'),
]