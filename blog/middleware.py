"""
Middleware pour initialiser automatiquement la base de données
"""
import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

class AutoInitializeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.initialized = False

    def __call__(self, request):
        # Initialiser la DB au premier appel
        if not self.initialized:
            try:
                self.initialize_database()
                self.initialized = True
            except Exception as e:
                logger.error(f"Erreur d'initialisation DB: {e}")
                # Continuer même en cas d'erreur
        
        response = self.get_response(request)
        return response

    def initialize_database(self):
        """Initialise la base de données si nécessaire"""
        try:
            # Vérifier si les tables existent
            from blog.models import Article
            Article.objects.count()
            logger.info("Base de données déjà initialisée")
        except Exception:
            logger.info("Initialisation de la base de données...")
            
            # Appliquer les migrations
            os.system("python manage.py migrate --noinput")
            
            # Peupler automatiquement (forcer pour Railway)
            os.system("python manage.py populate_blog")
            logger.info("Données d'exemple ajoutées")
            
            logger.info("Base de données initialisée avec succès")