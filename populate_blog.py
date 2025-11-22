"""
Script pour créer des données d'exemple pour le blog.
Usage: python manage.py shell < populate_blog.py
"""

from django.contrib.auth.models import User
from blog.models import Categorie, Article
from django.utils import timezone
from django.utils.text import slugify

# Créer un superutilisateur par défaut
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'is_staff': True,
        'is_superuser': True,
    }
)

if created:
    admin_user.set_password('admin123')
    admin_user.save()
    print("✓ Superutilisateur 'admin' créé (mot de passe: admin123)")
else:
    print("✓ Superutilisateur 'admin' existe déjà")

# Créer des catégories
categories_data = [
    {'nom': 'Technologie', 'description': 'Articles sur les nouvelles technologies', 'couleur': '#007bff'},
    {'nom': 'Développement Web', 'description': 'Tutoriels et conseils pour le développement web', 'couleur': '#28a745'},
    {'nom': 'Python', 'description': 'Tout sur le langage Python', 'couleur': '#fd7e14'},
    {'nom': 'Django', 'description': 'Framework web Django', 'couleur': '#6f42c1'},
    {'nom': 'Actualités', 'description': 'Dernières nouvelles du monde tech', 'couleur': '#dc3545'},
]

categories = []
for cat_data in categories_data:
    categorie, created = Categorie.objects.get_or_create(
        nom=cat_data['nom'],
        defaults=cat_data
    )
    categories.append(categorie)
    if created:
        print(f"✓ Catégorie '{categorie.nom}' créée")

# Créer des articles d'exemple
articles_data = [
    {
        'titre': 'Bienvenue sur mon blog Django',
        'contenu': '''Bienvenue sur ce blog créé avec Django !

Ce blog a été développé avec le framework web Django et propose plusieurs fonctionnalités intéressantes :

- **Gestion des articles** : Création, modification et publication d'articles
- **Système de catégories** : Organisation des articles par thématique
- **Commentaires** : Interaction avec les lecteurs
- **Interface d'administration** : Gestion facile du contenu
- **Design responsive** : Compatible avec tous les appareils

N'hésitez pas à explorer les différentes sections et à laisser des commentaires !''',
        'extrait': 'Découvrez ce nouveau blog créé avec Django et ses fonctionnalités.',
        'categorie': categories[3],  # Django
    },
    {
        'titre': 'Introduction à Django : Le framework web Python',
        'contenu': '''Django est un framework web Python de haut niveau qui encourage le développement rapide et propre.

## Pourquoi choisir Django ?

Django suit le principe "Don't Repeat Yourself" (DRY) et se concentre sur l'automatisation autant que possible. Il inclut :

1. **ORM intégré** : Interaction avec la base de données simplifiée
2. **Interface d'administration** : Générée automatiquement
3. **Système d'URL** : Routage élégant et flexible
4. **Système de templates** : Séparation logique/présentation
5. **Sécurité** : Protection CSRF, SQL injection, XSS

## Installation

Pour commencer avec Django :

```bash
pip install django
django-admin startproject monprojet
```

Django est utilisé par de nombreuses entreprises comme Instagram, Mozilla, et Pinterest !''',
        'extrait': 'Une introduction complète au framework web Django et ses avantages.',
        'categorie': categories[3],  # Django
    },
    {
        'titre': 'Les bases de Python pour débutants',
        'contenu': '''Python est un langage de programmation populaire, facile à apprendre et très polyvalent.

## Pourquoi Python ?

- **Syntaxe simple** : Facile à lire et à écrire
- **Polyvalent** : Web, data science, IA, automatisation
- **Grande communauté** : Nombreuses bibliothèques disponibles
- **Portable** : Fonctionne sur tous les systèmes

## Premier programme

```python
print("Hello, World!")
```

## Variables et types

```python
nom = "Alice"
age = 25
taille = 1.65
est_etudiant = True
```

Python est parfait pour commencer la programmation !''',
        'extrait': 'Apprenez les bases du langage Python avec ce guide pour débutants.',
        'categorie': categories[2],  # Python
    },
    {
        'titre': 'Responsive Design : Les meilleures pratiques',
        'contenu': '''Le responsive design est essentiel dans le développement web moderne.

## Qu'est-ce que le responsive design ?

Le responsive design permet à votre site web de s'adapter automatiquement à différentes tailles d'écran : ordinateurs, tablettes, smartphones.

## Techniques principales

### 1. Grille fluide
Utilisez des pourcentages plutôt que des pixels fixes :

```css
.container {
    width: 100%;
    max-width: 1200px;
}
```

### 2. Media queries
```css
@media (max-width: 768px) {
    .nav-menu {
        display: none;
    }
}
```

### 3. Images flexibles
```css
img {
    max-width: 100%;
    height: auto;
}
```

Ces techniques garantissent une expérience utilisateur optimale sur tous les appareils.''',
        'extrait': 'Maîtrisez les techniques du responsive design pour créer des sites web adaptatifs.',
        'categorie': categories[1],  # Développement Web
    },
    {
        'titre': 'L\'Intelligence Artificielle en 2024',
        'contenu': '''L'année 2024 marque un tournant dans le développement de l'Intelligence Artificielle.

## Tendances principales

### 1. IA Générative
- ChatGPT et ses alternatives
- Génération d'images (DALL-E, Midjourney)
- Génération de code automatisée

### 2. IA dans l'entreprise
- Automatisation des processus
- Analyse prédictive
- Assistants virtuels personnalisés

### 3. Éthique et régulation
- Nouvelles lois sur l'IA
- Questions de confidentialité
- Transparence des algorithmes

## Impact sur les développeurs

L'IA transforme notre façon de coder :
- Aide à la génération de code
- Détection automatique de bugs
- Optimisation des performances

Il est crucial de s'adapter à ces nouveaux outils tout en gardant un esprit critique.''',
        'extrait': 'Explorez les dernières tendances de l\'IA et leur impact sur le développement.',
        'categorie': categories[0],  # Technologie
    },
]

# Créer les articles
for i, article_data in enumerate(articles_data):
    article_data['slug'] = slugify(article_data['titre'])
    article_data['auteur'] = admin_user
    article_data['statut'] = 'published'
    
    article, created = Article.objects.get_or_create(
        titre=article_data['titre'],
        defaults=article_data
    )
    
    if created:
        print(f"✓ Article '{article.titre}' créé")

print(f"\n🎉 Blog initialisé avec {len(categories)} catégories et {len(articles_data)} articles !")
print("\nVous pouvez maintenant :")
print("1. Lancer le serveur : python manage.py runserver")
print("2. Accéder à l'admin : http://127.0.0.1:8000/admin/ (admin/admin123)")
print("3. Voir le blog : http://127.0.0.1:8000/")