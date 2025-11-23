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
            
            # Créer un superutilisateur automatiquement
            from django.contrib.auth.models import User
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='admin123'
                )
                logger.info("Superutilisateur créé : admin/admin123")
            
            # Peupler automatiquement (forcer pour Railway)
            os.system("python manage.py populate_blog")
            logger.info("Données d'exemple ajoutées")
            
            # Ajouter les cours Python
            self.create_sample_courses()
            logger.info("Cours Python ajoutés")
            
            logger.info("Base de données initialisée avec succès")

    def create_sample_courses(self):
        """Crée des cours d'exemple"""
        try:
            from blog.models import Cours, Chapitre
            
            # Cours 1: Python Débutant
            cours_debutant, created = Cours.objects.get_or_create(
                slug='python-debutant',
                defaults={
                    'titre': 'Python pour Débutants',
                    'description': 'Apprenez les bases de Python de zéro. Ce cours couvre les variables, les conditions, les boucles et les fonctions.',
                    'niveau': 'debutant',
                    'duree_estimee': 10,
                    'ordre': 1,
                    'actif': True
                }
            )
            
            if created:
                # Chapitres du cours débutant
                chapitres_debutant = [
                    {
                        'titre': 'Introduction à Python',
                        'slug': 'introduction-python',
                        'contenu': '''Python est un langage de programmation puissant et facile à apprendre.
                        
Il a été créé par Guido van Rossum en 1991 et est devenu l'un des langages les plus populaires au monde.

Pourquoi apprendre Python ?
- Syntaxe simple et lisible
- Polyvalent (web, data science, IA, etc.)
- Grande communauté
- Nombreuses bibliothèques''',
                        'code_exemple': '''# Votre premier programme Python
print("Bonjour le monde !")

# Python est facile à lire
nom = "Alice"
print(f"Salut {nom} !")''',
                        'exercice': '''Exercice 1: 
1. Créez une variable avec votre nom
2. Affichez un message de bienvenue personnalisé
3. Essayez d'afficher votre âge''',
                        'ordre': 0
                    },
                    {
                        'titre': 'Variables et Types',
                        'slug': 'variables-types',
                        'contenu': '''En Python, les variables stockent des données. Pas besoin de déclarer le type !
                        
Types de base :
- str : chaînes de caractères
- int : nombres entiers  
- float : nombres décimaux
- bool : True/False''',
                        'code_exemple': '''# Différents types de variables
nom = "Marie"           # String
age = 25               # Integer
taille = 1.65          # Float
majeur = True          # Boolean

# Vérifier le type
print(type(nom))       # <class 'str'>
print(type(age))       # <class 'int'>''',
                        'exercice': '''Exercice 2:
1. Créez des variables pour votre nom, âge et taille
2. Affichez le type de chaque variable
3. Calculez votre année de naissance''',
                        'ordre': 1
                    },
                    {
                        'titre': 'Conditions if/else',
                        'slug': 'conditions',
                        'contenu': '''Les conditions permettent d'exécuter du code selon certaines circonstances.
                        
Structure :
- if : si la condition est vraie
- elif : sinon si (autre condition)
- else : sinon (cas par défaut)''',
                        'code_exemple': '''age = 18

if age >= 18:
    print("Vous êtes majeur")
elif age >= 16:
    print("Vous pouvez conduire")
else:
    print("Vous êtes mineur")

# Conditions multiples
if age >= 18 and age < 65:
    print("En âge de travailler")''',
                        'exercice': '''Exercice 3:
1. Demandez l'âge de l'utilisateur
2. Affichez s'il peut voter (18+)
3. Ajoutez une condition pour la retraite (65+)''',
                        'ordre': 2
                    }
                ]
                
                for chapitre_data in chapitres_debutant:
                    Chapitre.objects.create(cours=cours_debutant, **chapitre_data)
            
            # Cours 2: Python Intermédiaire
            cours_inter, created = Cours.objects.get_or_create(
                slug='python-intermediaire',
                defaults={
                    'titre': 'Python Intermédiaire',
                    'description': 'Approfondissez vos connaissances avec les listes, dictionnaires, fonctions et classes.',
                    'niveau': 'intermediaire',
                    'duree_estimee': 15,
                    'ordre': 2,
                    'actif': True
                }
            )
            
            if created:
                chapitres_inter = [
                    {
                        'titre': 'Listes et Dictionnaires',
                        'slug': 'listes-dictionnaires',
                        'contenu': '''Les structures de données sont essentielles en Python.
                        
Listes : collections ordonnées
Dictionnaires : associations clé-valeur''',
                        'code_exemple': '''# Listes
fruits = ["pomme", "banane", "orange"]
fruits.append("kiwi")
print(fruits[0])  # "pomme"

# Dictionnaires  
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris"
}
print(personne["nom"])  # "Alice"''',
                        'exercice': '''Exercice: Créez un carnet d'adresses avec des dictionnaires''',
                        'ordre': 0
                    }
                ]
                
                for chapitre_data in chapitres_inter:
                    Chapitre.objects.create(cours=cours_inter, **chapitre_data)
                    
            logger.info("Cours d'exemple créés avec succès")
            
        except Exception as e:
            logger.error(f"Erreur lors de la création des cours: {e}")