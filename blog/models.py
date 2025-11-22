from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Categorie(models.Model):
    """Modèle pour les catégories d'articles"""
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    couleur = models.CharField(max_length=7, default='#007bff', help_text="Code couleur hexadécimal (ex: #ff0000)")
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['nom']
    
    def __str__(self):
        return self.nom


class Article(models.Model):
    """Modèle pour les articles de blog"""
    
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('published', 'Publié'),
    ]
    
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    contenu = models.TextField()
    extrait = models.TextField(max_length=300, help_text="Résumé de l'article (300 caractères max)")
    
    # Métadonnées
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    date_publication = models.DateTimeField(default=timezone.now)
    statut = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    # Relations
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    
    # SEO et engagement
    vues = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-date_publication']
        indexes = [
            models.Index(fields=['-date_publication']),
            models.Index(fields=['statut']),
        ]
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})
    
    def incrementer_vues(self):
        """Incrémente le compteur de vues"""
        self.vues += 1
        self.save(update_fields=['vues'])


class Commentaire(models.Model):
    """Modèle pour les commentaires des articles"""
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField(max_length=500)
    date_creation = models.DateTimeField(auto_now_add=True)
    actif = models.BooleanField(default=True, help_text="Décocher pour masquer le commentaire")
    
    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
        ordering = ['date_creation']
    
    def __str__(self):
        return f'Commentaire de {self.auteur.username} sur {self.article.titre}'