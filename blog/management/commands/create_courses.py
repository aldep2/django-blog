from django.core.management.base import BaseCommand
from blog.models import Cours, Chapitre
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crée les cours Python d\'exemple'

    def handle(self, *args, **options):
        """Crée les cours Python d'exemple"""
        
        # Récupérer l'admin comme auteur par défaut
        admin_user = User.objects.filter(is_superuser=True).first()
        if not admin_user:
            self.stdout.write(
                self.style.ERROR('Aucun superutilisateur trouvé. Créez-en un d\'abord.')
            )
            return
        
        # Cours 1: Python pour Débutants
        cours_debutant, created = Cours.objects.get_or_create(
            slug='python-debutant',
            defaults={
                'titre': 'Python pour Débutants',
                'description': 'Apprenez les bases de Python de zéro. Ce cours couvre l\'installation, les concepts fondamentaux et vos premiers programmes.',
                'niveau': 'debutant',
                'duree_estimee': 8,
                'ordre': 1,
                'actif': True
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Cours créé: {cours_debutant.titre}')
            )
        
        # Chapitre 1: Installation et premier code
        chapitre1, created = Chapitre.objects.get_or_create(
            cours=cours_debutant,
            slug='installation-premier-code',
            defaults={
                'titre': 'Installation et Premier Code',
                'ordre': 0,
                'contenu': '''# Installation et Premier Code Python

## 🐍 Qu'est-ce que Python ?

Python est un langage de programmation **facile à apprendre** et **très populaire**. Il est utilisé pour :
- Développement web (comme ce blog !)
- Intelligence artificielle
- Analyse de données  
- Automation de tâches
- Et bien plus encore !

## 💻 Installation de Python

### Étape 1: Télécharger Python
1. Allez sur **https://python.org**
2. Cliquez sur **"Download Python"** (la dernière version)
3. Téléchargez le fichier d'installation

### Étape 2: Installer Python
**Sur Windows :**
- Exécutez le fichier téléchargé
- ⚠️ **IMPORTANT** : Cochez "Add Python to PATH" 
- Cliquez sur "Install Now"

**Sur Mac :**
- Ouvrez le fichier .pkg téléchargé
- Suivez les instructions d'installation

**Sur Linux (Ubuntu/Debian) :**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Étape 3: Vérifier l'installation
Ouvrez votre terminal/invite de commandes et tapez :

```
python --version
```

Vous devriez voir quelque chose comme "Python 3.11.x"

## 🎯 Votre Premier Programme

### Méthode 1: Dans le terminal
1. Ouvrez votre terminal/invite de commandes
2. Tapez `python` et appuyez sur Entrée
3. Vous êtes maintenant dans l'interpréteur Python !

Essayez de taper ces commandes une par une :

```python
print("Hello, World!")
print("Bienvenue dans Python !")
2 + 3
"Python" + " est génial!"
```

Pour quitter l'interpréteur, tapez `exit()` ou `Ctrl+D`.

### Méthode 2: Créer un fichier Python
1. Créez un nouveau fichier appelé `mon_premier_programme.py`
2. Ouvrez-le dans un éditeur de texte (Notepad++, VSCode, etc.)
3. Écrivez votre code Python
4. Sauvegardez le fichier
5. Dans le terminal, naviguez vers le dossier du fichier
6. Exécutez avec : `python mon_premier_programme.py`

## 🛠️ Éditeurs recommandés

Pour écrire du Python plus facilement, installez un bon éditeur :

**Débutants :**
- **IDLE** (inclus avec Python)
- **Thonny** (parfait pour débuter)

**Plus avancés :**
- **Visual Studio Code** (gratuit, très populaire)
- **PyCharm** (professionnel)
- **Sublime Text**

## ✅ Récapitulatif

Vous avez maintenant :
1. ✅ Installé Python sur votre ordinateur
2. ✅ Vérifié que l'installation fonctionne  
3. ✅ Écrit votre premier programme "Hello World"
4. ✅ Découvert comment exécuter du code Python

**Prêt pour la suite ?** Dans le prochain chapitre, nous découvrirons les variables et les types de données !''',
                'code_exemple': '''# Votre premier programme Python
print("Hello, World!")
print("Bienvenue dans le monde de Python !")

# Faire des calculs simples
resultat = 2 + 3
print("2 + 3 =", resultat)

# Jouer avec du texte
nom = "Python"
message = nom + " est un langage fantastique !"
print(message)''',
                'exercice': '''## 🎯 Exercice Pratique

**Objectif :** Créer votre premier programme personnalisé

**Instructions :**
1. Créez un fichier appelé `presentation.py`
2. Écrivez un programme qui :
   - Affiche "Bonjour ! Je m'appelle [votre nom]"
   - Affiche votre âge (par exemple : "J'ai 25 ans")
   - Fait un calcul simple (par exemple votre année de naissance)
   - Affiche un message de motivation sur l'apprentissage de Python

**Exemple de résultat attendu :**
```
Bonjour ! Je m'appelle Alice
J'ai 25 ans
Je suis née en 1998
Python va m'aider à créer des choses incroyables !
```

**Bonus :** Ajoutez des emojis avec print("🐍 Python c'est génial ! 🎉")

**Solution :** Essayez d'abord par vous-même, puis comparez avec le code d'exemple !'''
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Chapitre créé: {chapitre1.titre}')
            )
        
        # Chapitre 2: Variables et types
        chapitre2, created = Chapitre.objects.get_or_create(
            cours=cours_debutant,
            slug='variables-et-types',
            defaults={
                'titre': 'Variables et Types de Données',
                'ordre': 1,
                'contenu': '''# Variables et Types de Données

## 📦 Qu'est-ce qu'une variable ?

Une **variable** est comme une boîte étiquetée où on peut stocker des informations. En Python, créer une variable est très simple !

## 🏷️ Créer des variables

```python
# Créer une variable avec du texte
nom = "Alice"
ville = "Paris"

# Créer une variable avec un nombre
age = 25
taille = 1.65

# Afficher les variables
print(nom)
print("J'habite à", ville)
```

## 🔢 Types de données principaux

### 1. **Chaînes de caractères (str)**
Pour stocker du texte :

```python
prenom = "Jean"
message = "Bonjour tout le monde !"
email = "jean@example.com"
```

### 2. **Nombres entiers (int)** 
Pour les nombres sans virgule :

```python
age = 30
nombre_enfants = 2
annee = 2024
```

### 3. **Nombres décimaux (float)**
Pour les nombres avec virgule :

```python
taille = 1.75
prix = 19.99
temperature = -5.5
```

### 4. **Booléens (bool)**
Pour vrai/faux :

```python
est_majeur = True
est_etudiant = False
```

## 🔍 Connaître le type d'une variable

Utilisez la fonction `type()` :

```python
nom = "Alice"
age = 25

print(type(nom))    # <class 'str'>
print(type(age))    # <class 'int'>
```

## 🔄 Conversion entre types

```python
# Convertir en chaîne
nombre = 42
nombre_texte = str(nombre)  # "42"

# Convertir en nombre
age_texte = "25"
age_nombre = int(age_texte)  # 25

# Convertir en décimal
prix_texte = "19.99"
prix_decimal = float(prix_texte)  # 19.99
```

## ⚠️ Règles importantes pour les noms de variables

**✅ Autorisé :**
```python
nom = "Alice"
age_utilisateur = 30
nombre_2 = 100
_secret = "password"
```

**❌ Interdit :**
```python
2nom = "Alice"      # Ne peut pas commencer par un chiffre
nom-utilisateur = 30  # Pas de tiret
class = "Python"    # Mot réservé de Python
```

## 🎯 Bonnes pratiques

1. **Noms descriptifs :** `age` plutôt que `a`
2. **Minuscules avec underscores :** `nom_utilisateur` 
3. **Pas d'espaces :** utilisez `_` à la place
4. **Évitez les accents** dans les noms de variables

## 💡 Variables multiples

```python
# Assigner plusieurs variables en une fois
nom, age, ville = "Alice", 25, "Paris"

# Échanger deux variables
a = 10
b = 20
a, b = b, a  # Maintenant a=20 et b=10
```''',
                'code_exemple': '''# Exemples de variables et types de données

# Variables texte
prenom = "Alice"
nom_famille = "Dupont"
profession = "Développeuse"

# Variables numériques
age = 28
salaire = 45000.50
nombre_projets = 12

# Variables booléennes
est_diplomee = True
travaille_remote = False

# Affichage des informations
print("=== Profil Utilisateur ===")
print("Nom complet:", prenom, nom_famille)
print("Profession:", profession)
print("Âge:", age, "ans")
print("Salaire:", salaire, "€")
print("Nombre de projets:", nombre_projets)
print("Diplômée:", est_diplomee)
print("Travail à distance:", travaille_remote)

print("\\n=== Types de données ===")
print("Type de 'prenom':", type(prenom))
print("Type de 'age':", type(age))
print("Type de 'salaire':", type(salaire))
print("Type de 'est_diplomee':", type(est_diplomee))

# Conversions
age_texte = str(age)
print("\\nÂge en texte:", age_texte)
print("Type après conversion:", type(age_texte))''',
                'exercice': '''## 🎯 Exercice : Créer votre profil

**Objectif :** Créer un programme qui stocke et affiche vos informations personnelles

**Instructions :**
1. Créez des variables pour stocker :
   - Votre prénom et nom de famille
   - Votre âge
   - Votre taille (en mètres, avec décimales)
   - Votre ville de résidence
   - Si vous êtes étudiant (vrai/faux)
   - Votre couleur préférée

2. Affichez toutes ces informations de manière organisée

3. Utilisez la fonction `type()` pour afficher le type de 3 variables

4. **Bonus :** Calculez votre année de naissance à partir de votre âge

**Exemple de sortie attendue :**
```
=== Mon Profil ===
Je m'appelle Alice Dupont
J'ai 25 ans
Je mesure 1.65 mètres
J'habite à Lyon
Étudiant : False
Couleur préférée : bleu

=== Types de données ===
Type du prénom : <class 'str'>
Type de l'âge : <class 'int'>
Type de la taille : <class 'float'>

Je suis probablement né(e) en 1998
```

**Conseils :**
- Utilisez des noms de variables descriptifs
- N'oubliez pas les guillemets pour le texte
- Pour l'année de naissance : `2024 - age`'''
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Chapitre créé: {chapitre2.titre}')
            )
        
        # Cours 2: Python Intermédiaire
        cours_inter, created = Cours.objects.get_or_create(
            slug='python-intermediaire',
            defaults={
                'titre': 'Python Intermédiaire',
                'description': 'Approfondissez vos connaissances Python avec les structures de données, les fonctions et la programmation orientée objet.',
                'niveau': 'intermediaire',
                'duree_estimee': 12,
                'ordre': 2,
                'actif': True
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Cours créé: {cours_inter.titre}')
            )
        
        self.stdout.write(
            self.style.SUCCESS('Tous les cours Python ont été créés avec succès !')
        )