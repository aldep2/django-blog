from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Categorie, Article, Commentaire


class BlogModelsTest(TestCase):
    """Tests des modèles du blog"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.categorie = Categorie.objects.create(
            nom='Test Catégorie',
            description='Une catégorie de test'
        )
    
    def test_creation_article(self):
        """Test de création d'un article"""
        article = Article.objects.create(
            titre='Article de test',
            slug='article-de-test',
            auteur=self.user,
            contenu='Contenu de l\'article de test',
            extrait='Extrait de test',
            categorie=self.categorie,
            statut='published'
        )
        
        self.assertEqual(str(article), 'Article de test')
        self.assertEqual(article.vues, 0)
        self.assertTrue(article.date_creation)
    
    def test_increment_vues(self):
        """Test d'incrémentation des vues"""
        article = Article.objects.create(
            titre='Article de test',
            slug='article-de-test',
            auteur=self.user,
            contenu='Contenu de test',
            extrait='Extrait de test',
            statut='published'
        )
        
        initial_vues = article.vues
        article.incrementer_vues()
        self.assertEqual(article.vues, initial_vues + 1)


class BlogViewsTest(TestCase):
    """Tests des vues du blog"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.categorie = Categorie.objects.create(
            nom='Test Catégorie',
            description='Une catégorie de test'
        )
        self.article = Article.objects.create(
            titre='Article de test',
            slug='article-de-test',
            auteur=self.user,
            contenu='Contenu de l\'article de test',
            extrait='Extrait de test',
            categorie=self.categorie,
            statut='published'
        )
    
    def test_liste_articles_view(self):
        """Test de la vue liste des articles"""
        response = self.client.get(reverse('blog:liste_articles'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Article de test')
    
    def test_detail_article_view(self):
        """Test de la vue détail d'article"""
        response = self.client.get(
            reverse('blog:article_detail', kwargs={'slug': self.article.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.article.titre)
        
        # Vérifier que les vues sont incrémentées
        self.article.refresh_from_db()
        self.assertEqual(self.article.vues, 1)
    
    def test_articles_par_categorie_view(self):
        """Test de la vue articles par catégorie"""
        response = self.client.get(
            reverse('blog:articles_par_categorie', kwargs={'categorie_id': self.categorie.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.categorie.nom)