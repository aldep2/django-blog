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
        
        # Chapitres pour le cours intermédiaire
        if created or not cours_inter.chapitres.exists():
            # Chapitre 1: Les listes
            Chapitre.objects.get_or_create(
                cours=cours_inter,
                slug='les-listes',
                defaults={
                    'titre': 'Les Listes en Python',
                    'ordre': 0,
                    'contenu': '''# Les Listes en Python

## 📋 Qu'est-ce qu'une liste ?

Une **liste** est une collection ordonnée d'éléments qui peuvent être de différents types. C'est l'une des structures de données les plus utiles en Python !

## 🏗️ Créer des listes

```python
# Liste vide
ma_liste = []
autre_liste = list()

# Liste avec des éléments
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = ["texte", 42, 3.14, True]
```

## 🔢 Accéder aux éléments

Les éléments d'une liste sont **indexés** à partir de 0 :

```python
fruits = ["pomme", "banane", "orange", "kiwi"]

print(fruits[0])    # "pomme" (premier élément)
print(fruits[1])    # "banane" (deuxième élément)
print(fruits[-1])   # "kiwi" (dernier élément)
print(fruits[-2])   # "orange" (avant-dernier)
```

## ✏️ Modifier une liste

```python
fruits = ["pomme", "banane", "orange"]

# Modifier un élément
fruits[1] = "mangue"
print(fruits)  # ["pomme", "mangue", "orange"]

# Ajouter un élément à la fin
fruits.append("kiwi")
print(fruits)  # ["pomme", "mangue", "orange", "kiwi"]

# Insérer à une position spécifique
fruits.insert(1, "fraise")
print(fruits)  # ["pomme", "fraise", "mangue", "orange", "kiwi"]

# Supprimer un élément
fruits.remove("mangue")
print(fruits)  # ["pomme", "fraise", "orange", "kiwi"]

# Supprimer par index
del fruits[0]
print(fruits)  # ["fraise", "orange", "kiwi"]
```

## 🔍 Méthodes utiles des listes

```python
nombres = [3, 1, 4, 1, 5, 9]

# Longueur de la liste
print(len(nombres))  # 6

# Trier la liste
nombres.sort()
print(nombres)  # [1, 1, 3, 4, 5, 9]

# Compter les occurrences
print(nombres.count(1))  # 2

# Trouver l'index d'un élément
print(nombres.index(4))  # 3

# Inverser la liste
nombres.reverse()
print(nombres)  # [9, 5, 4, 3, 1, 1]
```

## ✂️ Découpage de listes (slicing)

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sous-liste du début à l'index 5
print(nombres[:5])     # [0, 1, 2, 3, 4]

# Sous-liste de l'index 3 à la fin
print(nombres[3:])     # [3, 4, 5, 6, 7, 8, 9]

# Sous-liste de l'index 2 à 7
print(nombres[2:8])    # [2, 3, 4, 5, 6, 7]

# Tous les éléments avec un pas de 2
print(nombres[::2])    # [0, 2, 4, 6, 8]
```

## 🔄 Parcourir une liste

### Méthode 1: Parcours simple
```python
fruits = ["pomme", "banane", "orange"]

for fruit in fruits:
    print(f"J'aime les {fruit}s")
```

### Méthode 2: Avec index
```python
for i, fruit in enumerate(fruits):
    print(f"{i+1}. {fruit}")
```

## 📚 Listes de listes (matrices)

```python
# Créer une matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accéder à un élément
print(matrice[1][2])  # 6 (ligne 2, colonne 3)

# Parcourir une matrice
for ligne in matrice:
    for element in ligne:
        print(element, end=" ")
    print()  # Nouvelle ligne
```

## ⚡ List Comprehensions (avancé)

Une façon élégante de créer des listes :

```python
# Créer une liste des carrés de 0 à 9
carres = [x**2 for x in range(10)]
print(carres)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtrer les nombres pairs
pairs = [x for x in range(20) if x % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```''',
                    'code_exemple': '''# Exemple complet : Gestionnaire de tâches simple

# Créer une liste de tâches
taches = []

def afficher_menu():
    print("\\n=== GESTIONNAIRE DE TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Voir toutes les tâches")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")

def ajouter_tache():
    tache = input("Entrez une nouvelle tâche: ")
    taches.append(tache)
    print(f"Tâche '{tache}' ajoutée !")

def afficher_taches():
    if not taches:
        print("Aucune tâche dans la liste.")
    else:
        print("\\nVos tâches:")
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")

def supprimer_tache():
    if not taches:
        print("Aucune tâche à supprimer.")
        return
    
    afficher_taches()
    try:
        index = int(input("Numéro de la tâche à supprimer: ")) - 1
        if 0 <= index < len(taches):
            tache_supprimee = taches.pop(index)
            print(f"Tâche '{tache_supprimee}' supprimée !")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Programme principal
print("Bienvenue dans votre gestionnaire de tâches !")

while True:
    afficher_menu()
    choix = input("\\nVotre choix (1-5): ")
    
    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        print("Fonctionnalité à implémenter !")
    elif choix == "4":
        supprimer_tache()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")''',
                    'exercice': '''## 🎯 Exercice : Gestionnaire de notes d'étudiants

**Objectif :** Créer un programme pour gérer les notes d'une classe

**Instructions :**
1. Créez une liste vide appelée `notes`
2. Implémentez les fonctionnalités suivantes :
   - Ajouter une note (entre 0 et 20)
   - Afficher toutes les notes
   - Calculer la moyenne
   - Trouver la note la plus haute et la plus basse
   - Compter combien de notes sont au-dessus de la moyenne

**Fonctions à créer :**
```python
def ajouter_note(liste_notes):
    # Demander une note à l'utilisateur et l'ajouter à la liste
    pass

def calculer_moyenne(liste_notes):
    # Retourner la moyenne des notes
    pass

def afficher_statistiques(liste_notes):
    # Afficher moyenne, min, max, etc.
    pass
```

**Exemple d'utilisation :**
```
=== GESTIONNAIRE DE NOTES ===
Notes actuelles: [15, 12, 18, 9, 16]

Statistiques:
- Moyenne: 14.0
- Note la plus haute: 18
- Note la plus basse: 9
- Nombre de notes au-dessus de la moyenne: 2
```

**Bonus :**
- Ajouter une fonction pour supprimer une note
- Trier les notes par ordre croissant/décroissant
- Calculer la médiane

**Conseils :**
- Utilisez `sum(liste)` pour faire la somme
- Utilisez `len(liste)` pour la longueur
- Utilisez `max(liste)` et `min(liste)` pour les extrêmes'''
                }
            )
            
            # Chapitre 2: Les dictionnaires
            Chapitre.objects.get_or_create(
                cours=cours_inter,
                slug='les-dictionnaires',
                defaults={
                    'titre': 'Les Dictionnaires',
                    'ordre': 1,
                    'contenu': '''# Les Dictionnaires en Python

## 📖 Qu'est-ce qu'un dictionnaire ?

Un **dictionnaire** est une collection de paires **clé-valeur**. C'est comme un carnet d'adresses : chaque nom (clé) est associé à un numéro de téléphone (valeur).

## 🏗️ Créer des dictionnaires

```python
# Dictionnaire vide
mon_dict = {}
autre_dict = dict()

# Dictionnaire avec des éléments
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris"
}

# Différents types de clés et valeurs
mixte = {
    "texte": "valeur",
    42: "nombre comme clé",
    "liste": [1, 2, 3],
    "booleen": True
}
```

## 🔑 Accéder aux valeurs

```python
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris",
    "profession": "Développeuse"
}

# Accès direct
print(personne["nom"])        # "Alice"
print(personne["age"])        # 30

# Accès sécurisé avec get()
print(personne.get("ville"))  # "Paris"
print(personne.get("email"))  # None (pas d'erreur)
print(personne.get("email", "Non renseigné"))  # "Non renseigné"
```

## ✏️ Modifier un dictionnaire

```python
personne = {"nom": "Alice", "age": 30}

# Modifier une valeur existante
personne["age"] = 31

# Ajouter une nouvelle paire clé-valeur
personne["ville"] = "Lyon"
personne["profession"] = "Ingénieure"

print(personne)
# {"nom": "Alice", "age": 31, "ville": "Lyon", "profession": "Ingénieure"}

# Supprimer une clé
del personne["ville"]

# Supprimer et récupérer la valeur
profession = personne.pop("profession", "Non définie")
print(profession)  # "Ingénieure"
```

## 🔧 Méthodes utiles des dictionnaires

```python
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris"
}

# Obtenir toutes les clés
print(personne.keys())    # dict_keys(['nom', 'age', 'ville'])

# Obtenir toutes les valeurs
print(personne.values())  # dict_values(['Alice', 30, 'Paris'])

# Obtenir toutes les paires clé-valeur
print(personne.items())   # dict_items([('nom', 'Alice'), ('age', 30), ('ville', 'Paris')])

# Vérifier si une clé existe
print("nom" in personne)     # True
print("email" in personne)   # False

# Longueur du dictionnaire
print(len(personne))  # 3

# Copier un dictionnaire
copie = personne.copy()

# Vider un dictionnaire
personne.clear()
print(personne)  # {}
```

## 🔄 Parcourir un dictionnaire

### Parcourir les clés
```python
personne = {"nom": "Alice", "age": 30, "ville": "Paris"}

for cle in personne:
    print(f"Clé: {cle}")
```

### Parcourir les valeurs
```python
for valeur in personne.values():
    print(f"Valeur: {valeur}")
```

### Parcourir clés et valeurs ensemble
```python
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")
```

## 📚 Dictionnaires imbriqués

```python
# Base de données d'étudiants
etudiants = {
    "alice": {
        "age": 20,
        "notes": [15, 18, 12],
        "mention": "Bien"
    },
    "bob": {
        "age": 19,
        "notes": [10, 14, 16],
        "mention": "Assez Bien"
    }
}

# Accéder aux données imbriquées
print(etudiants["alice"]["age"])           # 20
print(etudiants["bob"]["notes"][0])        # 10

# Ajouter un nouvel étudiant
etudiants["charlie"] = {
    "age": 21,
    "notes": [17, 19, 20],
    "mention": "Très Bien"
}
```

## 💡 Cas d'usage pratiques

### Compteur de mots
```python
texte = "python est génial python est puissant"
mots = texte.split()

compteur = {}
for mot in mots:
    if mot in compteur:
        compteur[mot] += 1
    else:
        compteur[mot] = 1

print(compteur)  # {'python': 2, 'est': 2, 'génial': 1, 'puissant': 1}
```

### Configuration d'application
```python
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mon_app"
    },
    "debug": True,
    "version": "1.0.0"
}

def get_config(chemin):
    """Récupérer une valeur de config avec notation pointée"""
    keys = chemin.split(".")
    value = config
    for key in keys:
        value = value[key]
    return value

print(get_config("database.host"))  # "localhost"
```

## 🎯 Dictionnaire vs Liste

| Critère | Liste | Dictionnaire |
|---------|-------|-------------|
| **Accès** | Par index numérique | Par clé |
| **Ordre** | Maintenu (ordonné) | Maintenu depuis Python 3.7+ |
| **Modification** | Très rapide | Très rapide |
| **Recherche** | Lente (O(n)) | Très rapide (O(1)) |
| **Usage** | Séquences ordonnées | Associations clé-valeur |''',
                    'code_exemple': '''# Exemple complet : Carnet d'adresses avancé

# Base de données des contacts
contacts = {}

def afficher_menu():
    print("\\n=== CARNET D'ADRESSES ===")
    print("1. Ajouter un contact")
    print("2. Rechercher un contact")
    print("3. Afficher tous les contacts")
    print("4. Modifier un contact")
    print("5. Supprimer un contact")
    print("6. Statistiques")
    print("7. Quitter")

def ajouter_contact():
    nom = input("Nom du contact: ").strip().lower()
    if nom in contacts:
        print(f"Le contact '{nom}' existe déjà !")
        return
    
    contact = {
        "nom_complet": input("Nom complet: "),
        "telephone": input("Téléphone: "),
        "email": input("Email: "),
        "ville": input("Ville: "),
        "notes": input("Notes (optionnel): ")
    }
    
    contacts[nom] = contact
    print(f"Contact '{nom}' ajouté avec succès !")

def rechercher_contact():
    if not contacts:
        print("Aucun contact dans le carnet.")
        return
    
    nom = input("Nom à rechercher: ").strip().lower()
    if nom in contacts:
        contact = contacts[nom]
        print(f"\\n=== Contact trouvé ===")
        print(f"Nom: {contact['nom_complet']}")
        print(f"Téléphone: {contact['telephone']}")
        print(f"Email: {contact['email']}")
        print(f"Ville: {contact['ville']}")
        if contact['notes']:
            print(f"Notes: {contact['notes']}")
    else:
        print("Contact non trouvé.")

def afficher_tous_contacts():
    if not contacts:
        print("Aucun contact dans le carnet.")
        return
    
    print(f"\\n=== {len(contacts)} contact(s) ===")
    for nom, contact in contacts.items():
        print(f"• {contact['nom_complet']} - {contact['telephone']}")

def afficher_statistiques():
    if not contacts:
        print("Aucun contact pour les statistiques.")
        return
    
    print(f"\\n=== STATISTIQUES ===")
    print(f"Total contacts: {len(contacts)}")
    
    # Compter par ville
    villes = {}
    for contact in contacts.values():
        ville = contact['ville']
        if ville:
            villes[ville] = villes.get(ville, 0) + 1
    
    if villes:
        print("\\nRépartition par ville:")
        for ville, count in villes.items():
            print(f"  {ville}: {count} contact(s)")

# Programme principal
print("Bienvenue dans votre carnet d'adresses !")

while True:
    afficher_menu()
    choix = input("\\nVotre choix (1-7): ").strip()
    
    if choix == "1":
        ajouter_contact()
    elif choix == "2":
        rechercher_contact()
    elif choix == "3":
        afficher_tous_contacts()
    elif choix == "4":
        print("Fonctionnalité à implémenter !")
    elif choix == "5":
        nom = input("Nom du contact à supprimer: ").strip().lower()
        if nom in contacts:
            del contacts[nom]
            print("Contact supprimé !")
        else:
            print("Contact non trouvé.")
    elif choix == "6":
        afficher_statistiques()
    elif choix == "7":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")''',
                    'exercice': '''## 🎯 Exercice : Système de gestion d'inventaire

**Objectif :** Créer un programme pour gérer l'inventaire d'un magasin

**Structure des données :**
Utilisez un dictionnaire où chaque clé est le nom d'un produit et la valeur est un dictionnaire contenant:
- `prix`: prix unitaire
- `quantite`: quantité en stock
- `categorie`: catégorie du produit

**Fonctionnalités à implémenter :**
1. **Ajouter un produit** avec ses informations
2. **Afficher l'inventaire complet**
3. **Rechercher un produit** et afficher ses détails
4. **Mettre à jour le stock** (ajouter/retirer des quantités)
5. **Calculer la valeur totale** de l'inventaire
6. **Afficher les produits par catégorie**
7. **Trouver les produits en rupture de stock** (quantité = 0)

**Exemple de structure :**
```python
inventaire = {
    "laptop": {
        "prix": 899.99,
        "quantite": 5,
        "categorie": "informatique"
    },
    "souris": {
        "prix": 25.50,
        "quantite": 0,  # Rupture de stock
        "categorie": "informatique"
    }
}
```

**Fonctions suggérées :**
```python
def ajouter_produit(inventaire):
    # Demander les infos et ajouter le produit
    pass

def afficher_inventaire(inventaire):
    # Afficher tous les produits avec détails
    pass

def calculer_valeur_totale(inventaire):
    # Retourner: somme(prix * quantite) pour tous les produits
    pass

def produits_par_categorie(inventaire, categorie):
    # Retourner la liste des produits d'une catégorie
    pass
```

**Exemple de sortie attendue :**
```
=== INVENTAIRE MAGASIN ===
laptop (informatique): 5 unités à 899.99€ = 4499.95€
souris (informatique): RUPTURE DE STOCK (25.50€)

Valeur totale de l'inventaire: 4499.95€
Produits en rupture: souris
```

**Bonus :**
- Système d'alerte quand un produit a moins de 3 unités
- Sauvegarde/chargement depuis un fichier
- Recherche par fourchette de prix'''
                }
            )
            
            # Chapitre 3: Les fonctions
            Chapitre.objects.get_or_create(
                cours=cours_inter,
                slug='les-fonctions',
                defaults={
                    'titre': 'Les Fonctions Python',
                    'ordre': 2,
                    'contenu': '''# Les Fonctions en Python

## 🔧 Qu'est-ce qu'une fonction ?

Une **fonction** est un bloc de code réutilisable qui effectue une tâche spécifique. C'est comme avoir un outil dans votre boîte à outils !

## 📝 Définir une fonction simple

```python
def dire_bonjour():
    print("Bonjour ! Comment allez-vous ?")

# Appeler la fonction
dire_bonjour()  # Affiche: Bonjour ! Comment allez-vous ?
```

## 📥 Fonctions avec paramètres

```python
def dire_bonjour_personnalise(nom):
    print(f"Bonjour {nom} ! Comment allez-vous ?")

def additionner(a, b):
    resultat = a + b
    print(f"{a} + {b} = {resultat}")

# Utilisation
dire_bonjour_personnalise("Alice")  # Bonjour Alice !
additionner(5, 3)                   # 5 + 3 = 8
```

## 📤 Fonctions qui retournent des valeurs

```python
def calculer_carre(nombre):
    return nombre * nombre

def calculer_moyenne(notes):
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)

# Utilisation
carre = calculer_carre(5)
print(carre)  # 25

notes_etudiant = [15, 18, 12, 16]
moyenne = calculer_moyenne(notes_etudiant)
print(f"Moyenne: {moyenne}")  # Moyenne: 15.25
```

## 🎛️ Paramètres par défaut

```python
def presenter_personne(nom, age=0, ville="Non spécifiée"):
    print(f"Nom: {nom}")
    print(f"Âge: {age} ans")
    print(f"Ville: {ville}")

# Différents appels
presenter_personne("Alice")                    # Utilise les valeurs par défaut
presenter_personne("Bob", 25)                  # Spécifie l'âge
presenter_personne("Charlie", 30, "Paris")     # Spécifie tout
presenter_personne("Diana", ville="Lyon")      # Paramètre nommé
```

## 🏷️ Arguments nommés vs positionnels

```python
def creer_profil(nom, age, ville, profession):
    return {
        "nom": nom,
        "age": age,
        "ville": ville,
        "profession": profession
    }

# Arguments positionnels (ordre important)
profil1 = creer_profil("Alice", 30, "Paris", "Développeuse")

# Arguments nommés (ordre libre)
profil2 = creer_profil(
    profession="Designer",
    nom="Bob",
    ville="Lyon",
    age=25
)

print(profil1)
print(profil2)
```

## 📦 Fonctions avec nombre variable d'arguments

### *args (arguments positionnels)
```python
def additionner_tout(*nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    return total

# Utilisation
print(additionner_tout(1, 2, 3))           # 6
print(additionner_tout(10, 20, 30, 40))    # 100
```

### **kwargs (arguments nommés)
```python
def afficher_infos(**infos):
    print("Informations reçues:")
    for cle, valeur in infos.items():
        print(f"  {cle}: {valeur}")

# Utilisation
afficher_infos(nom="Alice", age=30, ville="Paris")
afficher_infos(produit="Laptop", prix=899, stock=5)
```

## 🔍 Portée des variables (scope)

```python
# Variable globale
compteur = 0

def incrementer():
    global compteur  # Indique qu'on veut modifier la variable globale
    compteur += 1
    print(f"Compteur: {compteur}")

def fonction_avec_variable_locale():
    variable_locale = "Je n'existe que dans cette fonction"
    print(variable_locale)

# Utilisation
incrementer()  # Compteur: 1
incrementer()  # Compteur: 2
fonction_avec_variable_locale()
# print(variable_locale)  # Erreur ! Variable non définie ici
```

## 📚 Fonctions comme objets

```python
def saluer(nom):
    return f"Salut {nom} !"

def remercier(nom):
    return f"Merci {nom} !"

# Stocker des fonctions dans une liste
actions = [saluer, remercier]

# Utiliser les fonctions
for action in actions:
    print(action("Alice"))

# Passer une fonction en paramètre
def executer_action(fonction, nom):
    return fonction(nom)

message = executer_action(saluer, "Bob")
print(message)  # Salut Bob !
```

## 🎯 Bonnes pratiques

### 1. Noms de fonctions descriptifs
```python
# ❌ Pas clair
def calc(x, y):
    return x * y

# ✅ Clair
def calculer_surface_rectangle(longueur, largeur):
    return longueur * largeur
```

### 2. Une fonction = une responsabilité
```python
# ❌ Fonction qui fait trop de choses
def traiter_utilisateur(nom, age, email):
    # Valider
    if not nom or not email:
        return False
    # Sauvegarder
    # Envoyer email
    # Logger
    # ...

# ✅ Fonctions spécialisées
def valider_utilisateur(nom, email):
    return bool(nom and email)

def sauvegarder_utilisateur(utilisateur):
    # Code de sauvegarde
    pass

def envoyer_email_bienvenue(email):
    # Code d'envoi email
    pass
```

### 3. Documentation des fonctions
```python
def calculer_imc(poids, taille):
    """
    Calcule l'Indice de Masse Corporelle.
    
    Args:
        poids (float): Poids en kilogrammes
        taille (float): Taille en mètres
    
    Returns:
        float: IMC calculé
        
    Example:
        >>> calculer_imc(70, 1.75)
        22.86
    """
    if taille <= 0:
        raise ValueError("La taille doit être positive")
    
    return poids / (taille ** 2)
```

## 🔄 Fonctions récursives (avancé)

```python
def factorielle(n):
    """Calcule n! de façon récursive"""
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

def fibonacci(n):
    """Calcule le nième terme de Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(factorielle(5))  # 120
print(fibonacci(7))    # 13
```''',
                    'code_exemple': '''# Exemple complet : Calculatrice modulaire avec fonctions

import math

def afficher_menu():
    """Affiche le menu principal de la calculatrice"""
    print("\\n=== CALCULATRICE PYTHON ===")
    print("1. Addition")
    print("2. Soustraction") 
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Racine carrée")
    print("7. Pourcentage")
    print("8. Historique")
    print("9. Quitter")

def demander_nombres(operation="calcul"):
    """Demande deux nombres à l'utilisateur avec validation"""
    try:
        a = float(input(f"Premier nombre pour {operation}: "))
        b = float(input(f"Deuxième nombre pour {operation}: "))
        return a, b
    except ValueError:
        print("Erreur: Veuillez entrer des nombres valides.")
        return None, None

def additionner(a, b):
    """Additionne deux nombres"""
    return a + b

def soustraire(a, b):
    """Soustrait b de a"""
    return a - b

def multiplier(a, b):
    """Multiplie deux nombres"""
    return a * b

def diviser(a, b):
    """Divise a par b avec gestion de la division par zéro"""
    if b == 0:
        return "Erreur: Division par zéro impossible"
    return a / b

def puissance(a, b):
    """Calcule a puissance b"""
    return a ** b

def racine_carree(nombre):
    """Calcule la racine carrée d'un nombre"""
    if nombre < 0:
        return "Erreur: Racine carrée d'un nombre négatif"
    return math.sqrt(nombre)

def calculer_pourcentage(valeur, pourcentage):
    """Calcule le pourcentage d'une valeur"""
    return (valeur * pourcentage) / 100

def enregistrer_calcul(operation, resultat, historique):
    """Enregistre un calcul dans l'historique"""
    historique.append(f"{operation} = {resultat}")

def afficher_historique(historique):
    """Affiche l'historique des calculs"""
    if not historique:
        print("Aucun calcul dans l'historique.")
        return
    
    print("\\n=== HISTORIQUE DES CALCULS ===")
    for i, calcul in enumerate(historique, 1):
        print(f"{i}. {calcul}")

def formater_resultat(resultat):
    """Formate le résultat pour un affichage propre"""
    if isinstance(resultat, float) and resultat.is_integer():
        return int(resultat)
    elif isinstance(resultat, float):
        return round(resultat, 4)
    return resultat

# Programme principal
def main():
    """Fonction principale de la calculatrice"""
    historique = []
    print("Bienvenue dans la calculatrice Python !")
    
    while True:
        afficher_menu()
        choix = input("\\nVotre choix (1-9): ").strip()
        
        if choix == "1":
            a, b = demander_nombres("addition")
            if a is not None and b is not None:
                resultat = additionner(a, b)
                resultat_formate = formater_resultat(resultat)
                print(f"Résultat: {a} + {b} = {resultat_formate}")
                enregistrer_calcul(f"{a} + {b}", resultat_formate, historique)
        
        elif choix == "2":
            a, b = demander_nombres("soustraction")
            if a is not None and b is not None:
                resultat = soustraire(a, b)
                resultat_formate = formater_resultat(resultat)
                print(f"Résultat: {a} - {b} = {resultat_formate}")
                enregistrer_calcul(f"{a} - {b}", resultat_formate, historique)
        
        elif choix == "3":
            a, b = demander_nombres("multiplication")
            if a is not None and b is not None:
                resultat = multiplier(a, b)
                resultat_formate = formater_resultat(resultat)
                print(f"Résultat: {a} × {b} = {resultat_formate}")
                enregistrer_calcul(f"{a} × {b}", resultat_formate, historique)
        
        elif choix == "4":
            a, b = demander_nombres("division")
            if a is not None and b is not None:
                resultat = diviser(a, b)
                if isinstance(resultat, str):  # Erreur
                    print(resultat)
                else:
                    resultat_formate = formater_resultat(resultat)
                    print(f"Résultat: {a} ÷ {b} = {resultat_formate}")
                    enregistrer_calcul(f"{a} ÷ {b}", resultat_formate, historique)
        
        elif choix == "6":
            try:
                nombre = float(input("Nombre pour racine carrée: "))
                resultat = racine_carree(nombre)
                if isinstance(resultat, str):  # Erreur
                    print(resultat)
                else:
                    resultat_formate = formater_resultat(resultat)
                    print(f"Résultat: √{nombre} = {resultat_formate}")
                    enregistrer_calcul(f"√{nombre}", resultat_formate, historique)
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide.")
        
        elif choix == "8":
            afficher_historique(historique)
        
        elif choix == "9":
            print("Merci d'avoir utilisé la calculatrice !")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")

# Lancer le programme
if __name__ == "__main__":
    main()''',
                    'exercice': '''## 🎯 Exercice : Système de gestion de bibliothèque

**Objectif :** Créer un système complet de gestion de bibliothèque avec des fonctions

**Fonctionnalités à implémenter :**

### 1. Structure des données
```python
# Liste globale des livres
bibliotheque = []

# Chaque livre est un dictionnaire:
livre = {
    "titre": "Le Petit Prince",
    "auteur": "Antoine de Saint-Exupéry",
    "annee": 1943,
    "pages": 96,
    "disponible": True
}
```

### 2. Fonctions à créer

**Gestion des livres :**
```python
def ajouter_livre(titre, auteur, annee, pages):
    """Ajoute un nouveau livre à la bibliothèque"""
    pass

def afficher_tous_livres():
    """Affiche tous les livres avec leurs détails"""
    pass

def rechercher_livre(titre):
    """Recherche un livre par titre (recherche partielle)"""
    pass

def supprimer_livre(titre):
    """Supprime un livre de la bibliothèque"""
    pass
```

**Gestion des emprunts :**
```python
def emprunter_livre(titre):
    """Marque un livre comme emprunté (disponible = False)"""
    pass

def rendre_livre(titre):
    """Marque un livre comme rendu (disponible = True)"""
    pass

def livres_disponibles():
    """Retourne la liste des livres disponibles"""
    pass

def livres_empruntes():
    """Retourne la liste des livres empruntés"""
    pass
```

**Statistiques :**
```python
def statistiques_bibliotheque():
    """Affiche des statistiques complètes"""
    # - Nombre total de livres
    # - Nombre de livres disponibles/empruntés
    # - Auteur le plus présent
    # - Livre le plus ancien/récent
    pass

def rechercher_par_auteur(auteur):
    """Trouve tous les livres d'un auteur"""
    pass

def livres_par_decennie():
    """Groupe les livres par décennie de publication"""
    pass
```

**Menu principal :**
```python
def afficher_menu():
    """Affiche le menu des options"""
    pass

def main():
    """Fonction principale avec boucle de menu"""
    pass
```

### 3. Fonctionnalités bonus

**Validation des données :**
```python
def valider_annee(annee):
    """Valide qu'une année est cohérente (1000-2024)"""
    pass

def valider_pages(pages):
    """Valide qu'un nombre de pages est positif"""
    pass
```

**Sauvegarde :**
```python
def sauvegarder_bibliotheque(nom_fichier="bibliotheque.txt"):
    """Sauvegarde la bibliothèque dans un fichier"""
    pass

def charger_bibliotheque(nom_fichier="bibliotheque.txt"):
    """Charge la bibliothèque depuis un fichier"""
    pass
```

### 4. Exemple d'utilisation

```
=== BIBLIOTHÈQUE PERSONNELLE ===
1. Ajouter un livre
2. Voir tous les livres
3. Rechercher un livre
4. Emprunter un livre
5. Rendre un livre  
6. Statistiques
7. Quitter

Votre choix: 2

=== TOUS LES LIVRES ===
1. "Le Petit Prince" par Antoine de Saint-Exupéry (1943) - 96 pages [DISPONIBLE]
2. "1984" par George Orwell (1949) - 328 pages [EMPRUNTÉ]

Total: 2 livres (1 disponible, 1 emprunté)
```

### 5. Conseils

- **Séparez les responsabilités** : une fonction = une tâche
- **Gérez les erreurs** : livre introuvable, déjà emprunté, etc.
- **Utilisez des fonctions utilitaires** pour éviter la répétition
- **Documentez vos fonctions** avec des docstrings
- **Testez chaque fonction** individuellement'''
                }
            )
        
        # Cours 3: Python Expert
        cours_expert, created = Cours.objects.get_or_create(
            slug='python-expert',
            defaults={
                'titre': 'Python Expert',
                'description': 'Maîtrisez les concepts avancés de Python : décorateurs, générateurs, métaclasses, programmation asynchrone et optimisation de performances.',
                'niveau': 'expert',
                'duree_estimee': 20,
                'ordre': 3,
                'actif': True
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Cours créé: {cours_expert.titre}')
            )
        
        # Chapitres pour le cours expert
        if created or not cours_expert.chapitres.exists():
            # Chapitre 1: Décorateurs et métaprogrammation
            Chapitre.objects.get_or_create(
                cours=cours_expert,
                slug='decorateurs-metaprogrammation',
                defaults={
                    'titre': 'Décorateurs et Métaprogrammation',
                    'ordre': 0,
                    'contenu': '''# Décorateurs et Métaprogrammation Python

## 🎭 Qu'est-ce qu'un décorateur ?

Un **décorateur** est une fonction qui modifie le comportement d'une autre fonction. C'est un concept puissant pour ajouter des fonctionnalités sans modifier le code original.

## 🔧 Décorateur simple

```python
def mon_decorateur(func):
    def wrapper():
        print("Quelque chose avant la fonction")
        func()
        print("Quelque chose après la fonction")
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

# Équivalent à:
# dire_bonjour = mon_decorateur(dire_bonjour)

dire_bonjour()
# Sortie:
# Quelque chose avant la fonction
# Bonjour !
# Quelque chose après la fonction
```

## ⏱️ Décorateur de mesure du temps

```python
import time
import functools

def mesurer_temps(func):
    @functools.wraps(func)  # Préserve les métadonnées de la fonction
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} a pris {fin - debut:.4f} secondes")
        return resultat
    return wrapper

@mesurer_temps
def calcul_lent():
    time.sleep(1)
    return sum(range(1000000))

resultat = calcul_lent()  # Affiche le temps d'exécution
```

## 🔐 Décorateur d'authentification

```python
def authentification_requise(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        utilisateur = kwargs.get('utilisateur')
        if not utilisateur or not utilisateur.get('connecte', False):
            print("Erreur: Authentification requise")
            return None
        return func(*args, **kwargs)
    return wrapper

@authentification_requise
def voir_profil(utilisateur=None):
    return f"Profil de {utilisateur['nom']}"

# Utilisation
user_connecte = {'nom': 'Alice', 'connecte': True}
user_non_connecte = {'nom': 'Bob', 'connecte': False}

print(voir_profil(utilisateur=user_connecte))      # Fonctionne
print(voir_profil(utilisateur=user_non_connecte))  # Erreur
```

## 🎛️ Décorateurs avec paramètres

```python
def retry(max_tentatives=3, delai=1):
    def decorateur(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for tentative in range(max_tentatives):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if tentative == max_tentatives - 1:
                        raise e
                    print(f"Tentative {tentative + 1} échouée: {e}")
                    time.sleep(delai)
        return wrapper
    return decorateur

@retry(max_tentatives=3, delai=0.5)
def operation_fragile():
    import random
    if random.random() < 0.7:  # 70% de chance d'échouer
        raise Exception("Opération échouée")
    return "Succès !"
```

## 🏭 Décorateurs de classe

```python
def singleton(classe):
    """Décorateur qui transforme une classe en singleton"""
    instances = {}
    
    @functools.wraps(classe)
    def get_instance(*args, **kwargs):
        if classe not in instances:
            instances[classe] = classe(*args, **kwargs)
        return instances[classe]
    
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Création de la connexion à la base de données")
        self.connected = True

# Test du singleton
db1 = DatabaseConnection()  # Crée l'instance
db2 = DatabaseConnection()  # Retourne la même instance
print(db1 is db2)  # True
```

## 📊 Property et descripteurs

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter pour les degrés Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, valeur):
        """Setter avec validation"""
        if valeur < -273.15:
            raise ValueError("Température en dessous du zéro absolu")
        self._celsius = valeur
    
    @property
    def fahrenheit(self):
        """Conversion automatique en Fahrenheit"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valeur):
        """Setter pour Fahrenheit qui met à jour Celsius"""
        self.celsius = (valeur - 32) * 5/9

# Utilisation
temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 100
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")
```

## 🔄 Métaclasses (très avancé)

```python
class AutoStringMeta(type):
    """Métaclasse qui ajoute automatiquement __str__ à toutes les classes"""
    def __new__(cls, name, bases, attrs):
        # Ajouter automatiquement une méthode __str__
        if '__str__' not in attrs:
            attrs['__str__'] = lambda self: f"Instance de {name}"
        
        return super().__new__(cls, name, bases, attrs)

class MaClasse(metaclass=AutoStringMeta):
    def __init__(self, valeur):
        self.valeur = valeur

obj = MaClasse(42)
print(obj)  # "Instance de MaClasse"
```

## 🎯 Décorateurs intégrés utiles

### @lru_cache - Cache LRU
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_optimise(n):
    if n < 2:
        return n
    return fibonacci_optimise(n-1) + fibonacci_optimise(n-2)

print(fibonacci_optimise(100))  # Très rapide grâce au cache
```

### @dataclass - Classes de données
```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Produit:
    nom: str
    prix: float
    categories: List[str] = field(default_factory=list)
    
    def prix_avec_tva(self, tva=0.20):
        return self.prix * (1 + tva)

produit = Produit("Laptop", 999.99, ["informatique", "bureau"])
print(produit)  # Représentation automatique
print(produit.prix_avec_tva())
```

## 💡 Bonnes pratiques

1. **Utilisez functools.wraps** pour préserver les métadonnées
2. **Gérez *args et **kwargs** pour la flexibilité
3. **Documentez vos décorateurs** clairement
4. **Testez avec et sans décorateurs**
5. **Évitez les décorateurs trop complexes**

Les décorateurs sont un outil puissant pour écrire du code plus propre et plus réutilisable !''',
                    'code_exemple': '''# Exemple complet : Système de cache et logging avancé

import functools
import time
import json
from datetime import datetime
from typing import Any, Dict, Callable

class CacheManager:
    """Gestionnaire de cache avancé avec TTL"""
    
    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}
    
    def get(self, key: str) -> Any:
        if key in self._cache:
            data = self._cache[key]
            if time.time() < data['expire']:
                return data['value']
            else:
                del self._cache[key]
        return None
    
    def set(self, key: str, value: Any, ttl: int = 300):
        """Définit une valeur dans le cache avec TTL en secondes"""
        self._cache[key] = {
            'value': value,
            'expire': time.time() + ttl,
            'created': datetime.now().isoformat()
        }
    
    def clear(self):
        """Vide le cache"""
        self._cache.clear()
    
    def stats(self):
        """Retourne les statistiques du cache"""
        return {
            'entries': len(self._cache),
            'keys': list(self._cache.keys())
        }

# Instance globale du cache
cache_manager = CacheManager()

def cache_with_ttl(ttl: int = 300):
    """Décorateur de cache avec Time To Live"""
    def decorateur(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Créer une clé unique basée sur le nom de la fonction et les arguments
            cache_key = f"{func.__name__}:{hash(str(args) + str(sorted(kwargs.items())))}"
            
            # Vérifier le cache
            cached_result = cache_manager.get(cache_key)
            if cached_result is not None:
                print(f"🎯 Cache HIT pour {func.__name__}")
                return cached_result
            
            # Exécuter la fonction et mettre en cache
            print(f"⚡ Cache MISS pour {func.__name__} - Exécution...")
            result = func(*args, **kwargs)
            cache_manager.set(cache_key, result, ttl)
            
            return result
        return wrapper
    return decorateur

def log_calls(log_args: bool = True, log_result: bool = True):
    """Décorateur de logging avancé"""
    def decorateur(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            log_info = {
                'function': func.__name__,
                'timestamp': timestamp,
                'module': func.__module__
            }
            
            if log_args and (args or kwargs):
                log_info['arguments'] = {
                    'args': args,
                    'kwargs': kwargs
                }
            
            print(f"📝 [{timestamp}] Appel de {func.__name__}")
            
            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                
                log_info['status'] = 'SUCCESS'
                log_info['execution_time'] = f"{execution_time:.4f}s"
                
                if log_result:
                    log_info['result'] = str(result)[:100]  # Limiter la taille
                
                print(f"✅ {func.__name__} terminé en {execution_time:.4f}s")
                return result
                
            except Exception as e:
                log_info['status'] = 'ERROR'
                log_info['error'] = str(e)
                print(f"❌ Erreur dans {func.__name__}: {e}")
                raise
                
        return wrapper
    return decorateur

def rate_limit(max_calls: int, period: int = 60):
    """Décorateur de limitation de débit"""
    call_times = []
    
    def decorateur(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            
            # Nettoyer les appels anciens
            call_times[:] = [t for t in call_times if now - t < period]
            
            if len(call_times) >= max_calls:
                raise Exception(f"Rate limit dépassé: {max_calls} appels par {period}s")
            
            call_times.append(now)
            return func(*args, **kwargs)
            
        return wrapper
    return decorateur

# Exemples d'utilisation des décorateurs

@cache_with_ttl(ttl=60)  # Cache pendant 1 minute
@log_calls(log_args=True, log_result=True)
def fibonacci_lent(n: int) -> int:
    """Calcul de Fibonacci volontairement lent pour démontrer le cache"""
    if n <= 1:
        return n
    time.sleep(0.1)  # Simulation d'une opération lente
    return fibonacci_lent(n-1) + fibonacci_lent(n-2)

@rate_limit(max_calls=3, period=10)  # Max 3 appels par 10 secondes
@log_calls(log_args=False, log_result=True)
def api_call_simulee(endpoint: str) -> dict:
    """Simulation d'un appel API avec limitation de débit"""
    time.sleep(0.5)  # Simulation latence réseau
    return {
        'endpoint': endpoint,
        'status': 200,
        'data': f"Données de {endpoint}",
        'timestamp': datetime.now().isoformat()
    }

@cache_with_ttl(ttl=30)
def calcul_complexe(x: int, y: int) -> float:
    """Simulation d'un calcul complexe"""
    print(f"Exécution du calcul complexe avec {x} et {y}")
    time.sleep(1)  # Simulation d'un calcul long
    return (x ** 2 + y ** 2) ** 0.5

def demo_decorateurs():
    """Démonstration des décorateurs en action"""
    print("=== DÉMONSTRATION DES DÉCORATEURS ===\\n")
    
    # Test du cache
    print("1. Test du système de cache:")
    print(f"Premier appel: {calcul_complexe(3, 4)}")
    print(f"Deuxième appel (depuis le cache): {calcul_complexe(3, 4)}")
    print(f"Statistiques du cache: {cache_manager.stats()}\\n")
    
    # Test du rate limiting
    print("2. Test du rate limiting:")
    try:
        for i in range(5):
            result = api_call_simulee(f"users/{i}")
            print(f"Appel {i+1} réussi")
    except Exception as e:
        print(f"Rate limit atteint: {e}\\n")
    
    # Test du logging avec Fibonacci
    print("3. Test du cache avec Fibonacci:")
    print(f"fibonacci_lent(5) première fois:")
    result1 = fibonacci_lent(5)
    print(f"Résultat: {result1}")
    
    print(f"\\nfibonacci_lent(5) deuxième fois (cache):")
    result2 = fibonacci_lent(5)
    print(f"Résultat: {result2}")

if __name__ == "__main__":
    demo_decorateurs()''',
                    'exercice': '''## 🎯 Exercice Expert : Système de décorateurs pour API REST

**Objectif :** Créer un ensemble de décorateurs pour sécuriser et optimiser une API REST

### 1. Décorateurs à implémenter

**a) @api_key_required**
```python
def api_key_required(valid_keys=None):
    """
    Vérifie qu'une clé API valide est fournie
    valid_keys: liste des clés API valides
    """
    pass

# Usage:
@api_key_required(['abc123', 'xyz789'])
def get_user_data(user_id, api_key=None):
    return f"Données utilisateur {user_id}"
```

**b) @validate_json**
```python
def validate_json(schema):
    """
    Valide que les données JSON respectent un schéma
    schema: dictionnaire définissant les champs requis
    """
    pass

# Usage:
@validate_json({'name': str, 'age': int, 'email': str})
def create_user(data):
    return f"Utilisateur {data['name']} créé"
```

**c) @cache_response**
```python
def cache_response(ttl=300, key_func=None):
    """
    Met en cache les réponses avec TTL personnalisable
    key_func: fonction pour générer la clé de cache
    """
    pass
```

**d) @require_role**
```python
def require_role(*required_roles):
    """
    Vérifie que l'utilisateur a l'un des rôles requis
    """
    pass

# Usage:
@require_role('admin', 'moderator')
def delete_user(user_id, current_user=None):
    return f"Utilisateur {user_id} supprimé"
```

### 2. Contexte de l'exercice

Créez une simulation d'API REST avec ces décorateurs :

```python
# Données de test
VALID_API_KEYS = ['dev123', 'prod456', 'test789']

USERS_DB = [
    {'id': 1, 'name': 'Alice', 'role': 'admin', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'role': 'user', 'email': 'bob@example.com'},
    {'id': 3, 'name': 'Charlie', 'role': 'moderator', 'email': 'charlie@example.com'}
]

# Endpoints à protéger
@api_key_required(VALID_API_KEYS)
@cache_response(ttl=60)
def get_users(api_key=None):
    """Récupérer tous les utilisateurs"""
    pass

@api_key_required(VALID_API_KEYS)
@require_role('admin')
@validate_json({'name': str, 'email': str, 'role': str})
def create_user(data, api_key=None, current_user=None):
    """Créer un nouvel utilisateur"""
    pass
```

### 3. Fonctionnalités bonus

**a) Décorateur de monitoring**
```python
@monitor_performance
def slow_endpoint():
    """Surveille les performances et alerte si > 2 secondes"""
    pass
```

**b) Décorateur d'audit**
```python
@audit_log
def sensitive_operation(data, current_user=None):
    """Log toutes les opérations sensibles"""
    pass
```

**c) Décorateur de retry avec backoff**
```python
@retry_with_backoff(max_retries=3, backoff_factor=2)
def unreliable_external_api():
    """Retry automatique avec délai exponentiel"""
    pass
```

### 4. Tests à créer

```python
def test_decorators():
    # Test API key
    assert get_users(api_key='dev123') is not None
    
    try:
        get_users(api_key='invalid')
        assert False, "Devrait lever une exception"
    except Exception:
        pass
    
    # Test validation JSON
    valid_data = {'name': 'Test', 'email': 'test@test.com', 'role': 'user'}
    invalid_data = {'name': 'Test'}  # email manquant
    
    # Test rôles
    admin_user = {'role': 'admin'}
    user_user = {'role': 'user'}
    
    # ... plus de tests
```

### 5. Exemple d'utilisation complète

```python
def simulate_api_requests():
    print("=== SIMULATION API REST ===")
    
    # Requête valide
    try:
        users = get_users(api_key='dev123')
        print(f"✅ Utilisateurs récupérés: {len(users)}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Requête avec clé invalide
    try:
        users = get_users(api_key='invalid')
    except Exception as e:
        print(f"❌ Clé API invalide: {e}")
    
    # Création d'utilisateur (admin requis)
    admin_user = {'role': 'admin', 'name': 'Admin'}
    new_user_data = {
        'name': 'Nouvel Utilisateur',
        'email': 'nouveau@example.com',
        'role': 'user'
    }
    
    try:
        result = create_user(
            data=new_user_data,
            api_key='dev123',
            current_user=admin_user
        )
        print(f"✅ Utilisateur créé: {result}")
    except Exception as e:
        print(f"❌ Erreur création: {e}")
```

### 6. Critères d'évaluation

- **Sécurité** : Validation correcte des permissions
- **Performance** : Cache efficace et rate limiting
- **Robustesse** : Gestion d'erreurs complète
- **Flexibilité** : Décorateurs configurables
- **Lisibilité** : Code clair et bien documenté

Cet exercice teste votre maîtrise des décorateurs avancés et des concepts de sécurité API !'''
                }
            )
            
            # Chapitre 2: Générateurs et itérateurs
            Chapitre.objects.get_or_create(
                cours=cours_expert,
                slug='generateurs-iterateurs',
                defaults={
                    'titre': 'Générateurs et Itérateurs',
                    'ordre': 1,
                    'contenu': '''# Générateurs et Itérateurs Python

## 🔄 Qu'est-ce qu'un itérateur ?

Un **itérateur** est un objet qui permet de parcourir une séquence d'éléments un par un, sans charger tous les éléments en mémoire simultanément.

## 📝 Protocole d'itération

```python
class MonIterateur:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_val:
            self.current += 1
            return self.current
        raise StopIteration

# Utilisation
for nombre in MonIterateur(5):
    print(nombre)  # Affiche 1, 2, 3, 4, 5
```

## ⚡ Générateurs : la syntaxe simple

Les **générateurs** sont une façon élégante de créer des itérateurs avec `yield`.

```python
def compter_jusqu_a(n):
    """Générateur qui compte de 1 à n"""
    i = 1
    while i <= n:
        yield i  # Pause ici et retourne i
        i += 1

# Utilisation
for nombre in compter_jusqu_a(3):
    print(nombre)
# Affiche: 1, 2, 3

# Le générateur peut être réutilisé
gen = compter_jusqu_a(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # StopIteration
```

## 🚀 Avantages des générateurs

### Économie mémoire
```python
# ❌ Liste normale - charge tout en mémoire
def nombres_carres_liste(n):
    return [i**2 for i in range(n)]

# ✅ Générateur - un élément à la fois
def nombres_carres_gen(n):
    for i in range(n):
        yield i**2

# Comparaison mémoire
import sys
liste = nombres_carres_liste(1000000)
print(f"Liste: {sys.getsizeof(liste)} bytes")

gen = nombres_carres_gen(1000000)
print(f"Générateur: {sys.getsizeof(gen)} bytes")
```

### Évaluation paresseuse (lazy evaluation)
```python
def fibonacci():
    """Générateur infini de nombres de Fibonacci"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Prendre seulement les 10 premiers
fib = fibonacci()
premiers_dix = [next(fib) for _ in range(10)]
print(premiers_dix)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 🔧 Générateurs avec send() et close()

```python
def calculatrice():
    """Générateur qui agit comme une calculatrice"""
    resultat = 0
    while True:
        operation = yield resultat
        if operation is None:
            continue
        
        if operation[0] == '+':
            resultat += operation[1]
        elif operation[0] == '-':
            resultat -= operation[1]
        elif operation[0] == '*':
            resultat *= operation[1]
        elif operation[0] == 'reset':
            resultat = 0

# Utilisation
calc = calculatrice()
next(calc)  # Démarrer le générateur

print(calc.send(('+', 10)))  # 10
print(calc.send(('*', 2)))   # 20
print(calc.send(('-', 5)))   # 15
print(calc.send(('reset', 0)))  # 0
```

## 📊 Expressions génératrices

```python
# Générateur inline (generator expression)
carres = (x**2 for x in range(10))
print(type(carres))  # <class 'generator'>

# Utilisation avec fonctions built-in
print(sum(x**2 for x in range(10)))  # Somme des carrés

# Pipeline de générateurs
def nombres():
    for i in range(100):
        yield i

def pairs(source):
    for item in source:
        if item % 2 == 0:
            yield item

def carres(source):
    for item in source:
        yield item ** 2

# Chaînage élégant
pipeline = carres(pairs(nombres()))
premiers_cinq = [next(pipeline) for _ in range(5)]
print(premiers_cinq)  # [0, 4, 16, 36, 64]
```

## 🔄 yield from - Délégation de générateurs

```python
def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield 'a'
    yield 'b'
    yield 'c'

def combine_generators():
    yield from gen1()  # Délègue à gen1
    yield from gen2()  # Puis à gen2
    yield 'fin'

for item in combine_generators():
    print(item)
# Affiche: 1, 2, 3, a, b, c, fin
```

## 📁 Générateurs pour traitement de fichiers

```python
def lire_fichier_par_chunks(nom_fichier, taille_chunk=1024):
    """Générateur pour lire un gros fichier par morceaux"""
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(taille_chunk)
            if not chunk:
                break
            yield chunk

def compter_mots_gros_fichier(nom_fichier):
    """Compte les mots dans un gros fichier sans tout charger"""
    compteur = 0
    for chunk in lire_fichier_par_chunks(nom_fichier):
        compteur += len(chunk.split())
    return compteur

def filtrer_lignes(nom_fichier, mot_cle):
    """Générateur qui filtre les lignes contenant un mot-clé"""
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        for ligne in f:
            if mot_cle in ligne:
                yield ligne.strip()
```

## 🌐 Générateurs pour scraping web

```python
def paginer_api(url_base, max_pages=None):
    """Générateur pour paginer une API REST"""
    page = 1
    while max_pages is None or page <= max_pages:
        url = f"{url_base}?page={page}"
        # response = requests.get(url)  # Simulation
        # data = response.json()
        
        # Simulation de données
        data = {
            'items': [f'item_{page}_{i}' for i in range(3)],
            'has_next': page < 5
        }
        
        for item in data['items']:
            yield item
        
        if not data.get('has_next', False):
            break
        page += 1

# Utilisation
for item in paginer_api('https://api.example.com/items', max_pages=3):
    print(item)
```

## 🔍 Générateurs avancés avec état

```python
class StatefulGenerator:
    """Générateur avec état persistant"""
    
    def __init__(self, start=0):
        self.value = start
        self.history = []
    
    def counter(self):
        while True:
            self.history.append(self.value)
            yield self.value
            self.value += 1
    
    def get_stats(self):
        return {
            'current': self.value,
            'history_length': len(self.history),
            'sum': sum(self.history)
        }

# Utilisation
gen_obj = StatefulGenerator(10)
counter = gen_obj.counter()

print(next(counter))  # 10
print(next(counter))  # 11
print(next(counter))  # 12
print(gen_obj.get_stats())  # Stats avec historique
```

## ⚡ Performance : générateurs vs listes

```python
import time
import memory_profiler

def benchmark_performance():
    """Compare performance générateur vs liste"""
    
    # Test mémoire
    def process_liste(n):
        return sum([x**2 for x in range(n)])
    
    def process_gen(n):
        return sum(x**2 for x in range(n))
    
    # Test vitesse
    n = 1000000
    
    start = time.time()
    result_liste = process_liste(n)
    time_liste = time.time() - start
    
    start = time.time()
    result_gen = process_gen(n)
    time_gen = time.time() - start
    
    print(f"Liste: {time_liste:.4f}s - Résultat: {result_liste}")
    print(f"Générateur: {time_gen:.4f}s - Résultat: {result_gen}")
    
    # Les deux donnent le même résultat, mais le générateur utilise moins de mémoire
```

## 🎯 Cas d'usage idéaux pour les générateurs

1. **Traitement de gros fichiers**
2. **Pagination d'APIs**
3. **Pipelines de données**
4. **Séquences infinies**
5. **Parsing de flux de données**
6. **Algorithmes de recherche**

Les générateurs sont essentiels pour écrire du Python efficace en mémoire !''',
                    'code_exemple': '''# Exemple complet : Pipeline de traitement de données avec générateurs

import json
import csv
import time
import random
from typing import Generator, Dict, Any, List
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    message: str
    user_id: int
    ip_address: str
    endpoint: str
    response_time: float

class DataPipeline:
    """Pipeline de traitement de données utilisant des générateurs"""
    
    def __init__(self):
        self.processed_count = 0
        self.errors_count = 0
    
    def generate_sample_logs(self, count: int = 1000) -> Generator[Dict[str, Any], None, None]:
        """Générateur de logs d'exemple pour simulation"""
        levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
        endpoints = ['/api/users', '/api/orders', '/api/products', '/login', '/logout']
        messages = ['Request processed', 'Database query', 'User action', 'System error']
        
        start_time = datetime.now() - timedelta(days=7)
        
        for i in range(count):
            timestamp = start_time + timedelta(
                seconds=random.randint(0, 7 * 24 * 60 * 60)
            )
            
            yield {
                'timestamp': timestamp.isoformat(),
                'level': random.choice(levels),
                'message': random.choice(messages),
                'user_id': random.randint(1, 1000),
                'ip_address': f"192.168.1.{random.randint(1, 255)}",
                'endpoint': random.choice(endpoints),
                'response_time': round(random.uniform(0.01, 2.0), 3)
            }
    
    def parse_log_data(self, raw_logs: Generator) -> Generator[LogEntry, None, None]:
        """Parse les données de log brutes en objets LogEntry"""
        for log_dict in raw_logs:
            try:
                log_entry = LogEntry(
                    timestamp=datetime.fromisoformat(log_dict['timestamp']),
                    level=log_dict['level'],
                    message=log_dict['message'],
                    user_id=log_dict['user_id'],
                    ip_address=log_dict['ip_address'],
                    endpoint=log_dict['endpoint'],
                    response_time=log_dict['response_time']
                )
                yield log_entry
                self.processed_count += 1
                
            except (KeyError, ValueError) as e:
                print(f"Erreur de parsing: {e}")
                self.errors_count += 1
                continue
    
    def filter_by_level(self, logs: Generator[LogEntry, None, None], 
                       levels: List[str]) -> Generator[LogEntry, None, None]:
        """Filtre les logs par niveau"""
        for log in logs:
            if log.level in levels:
                yield log
    
    def filter_by_response_time(self, logs: Generator[LogEntry, None, None], 
                              min_time: float = 0.0) -> Generator[LogEntry, None, None]:
        """Filtre les logs par temps de réponse minimum"""
        for log in logs:
            if log.response_time >= min_time:
                yield log
    
    def group_by_endpoint(self, logs: Generator[LogEntry, None, None]) -> Generator[Dict[str, List[LogEntry]], None, None]:
        """Groupe les logs par endpoint"""
        current_batch = {}
        batch_size = 100
        count = 0
        
        for log in logs:
            endpoint = log.endpoint
            if endpoint not in current_batch:
                current_batch[endpoint] = []
            
            current_batch[endpoint].append(log)
            count += 1
            
            # Yield par batch pour éviter de charger trop en mémoire
            if count >= batch_size:
                yield current_batch
                current_batch = {}
                count = 0
        
        # Yield le dernier batch s'il n'est pas vide
        if current_batch:
            yield current_batch
    
    def calculate_stats(self, log_groups: Generator) -> Generator[Dict[str, Any], None, None]:
        """Calcule les statistiques pour chaque groupe d'endpoints"""
        for batch in log_groups:
            stats = {}
            
            for endpoint, logs in batch.items():
                if not logs:
                    continue
                
                response_times = [log.response_time for log in logs]
                error_count = sum(1 for log in logs if log.level == 'ERROR')
                
                stats[endpoint] = {
                    'total_requests': len(logs),
                    'avg_response_time': sum(response_times) / len(response_times),
                    'max_response_time': max(response_times),
                    'min_response_time': min(response_times),
                    'error_rate': error_count / len(logs) * 100,
                    'unique_users': len(set(log.user_id for log in logs))
                }
            
            yield stats
    
    def save_to_json(self, stats_gen: Generator, filename: str = 'stats.json'):
        """Sauvegarde les statistiques en JSON"""
        all_stats = {}
        
        for batch_stats in stats_gen:
            for endpoint, stats in batch_stats.items():
                if endpoint in all_stats:
                    # Combine les stats si l'endpoint existe déjà
                    existing = all_stats[endpoint]
                    total_req = existing['total_requests'] + stats['total_requests']
                    
                    all_stats[endpoint] = {
                        'total_requests': total_req,
                        'avg_response_time': (
                            existing['avg_response_time'] * existing['total_requests'] +
                            stats['avg_response_time'] * stats['total_requests']
                        ) / total_req,
                        'max_response_time': max(existing['max_response_time'], stats['max_response_time']),
                        'min_response_time': min(existing['min_response_time'], stats['min_response_time']),
                        'error_rate': (
                            existing['error_rate'] * existing['total_requests'] +
                            stats['error_rate'] * stats['total_requests']
                        ) / total_req,
                        'unique_users': existing['unique_users'] + stats['unique_users']  # Approximation
                    }
                else:
                    all_stats[endpoint] = stats
        
        with open(filename, 'w') as f:
            json.dump(all_stats, f, indent=2, default=str)
        
        return all_stats

def infinite_data_stream():
    """Générateur infini pour simulation de stream de données"""
    counter = 0
    while True:
        yield {
            'id': counter,
            'timestamp': datetime.now().isoformat(),
            'value': random.randint(1, 100),
            'category': random.choice(['A', 'B', 'C'])
        }
        counter += 1
        time.sleep(0.1)  # Simulation délai réseau

def process_stream_with_window(stream_gen: Generator, window_size: int = 10):
    """Traite un stream avec une fenêtre glissante"""
    window = []
    
    for data in stream_gen:
        window.append(data)
        
        if len(window) >= window_size:
            # Traiter la fenêtre
            avg_value = sum(item['value'] for item in window) / len(window)
            categories = set(item['category'] for item in window)
            
            yield {
                'window_avg': avg_value,
                'categories_count': len(categories),
                'window_size': len(window),
                'latest_timestamp': window[-1]['timestamp']
            }
            
            # Glisser la fenêtre (retirer le plus ancien)
            window.pop(0)

def demo_pipeline():
    """Démonstration complète du pipeline de données"""
    print("=== PIPELINE DE TRAITEMENT DE DONNÉES ===\\n")
    
    pipeline = DataPipeline()
    
    # Étape 1: Générer des données
    print("1. Génération de 10000 logs simulés...")
    raw_logs = pipeline.generate_sample_logs(10000)
    
    # Étape 2: Parser les données
    print("2. Parsing des logs...")
    parsed_logs = pipeline.parse_log_data(raw_logs)
    
    # Étape 3: Filtrer par niveau d'erreur
    print("3. Filtrage des logs ERROR et WARNING...")
    filtered_logs = pipeline.filter_by_level(parsed_logs, ['ERROR', 'WARNING'])
    
    # Étape 4: Filtrer par temps de réponse lent
    print("4. Filtrage des réponses lentes (>0.5s)...")
    slow_logs = pipeline.filter_by_response_time(filtered_logs, 0.5)
    
    # Étape 5: Grouper par endpoint
    print("5. Groupement par endpoint...")
    grouped_logs = pipeline.group_by_endpoint(slow_logs)
    
    # Étape 6: Calculer les statistiques
    print("6. Calcul des statistiques...")
    stats = pipeline.calculate_stats(grouped_logs)
    
    # Étape 7: Sauvegarder
    print("7. Sauvegarde des résultats...")
    final_stats = pipeline.save_to_json(stats, 'pipeline_results.json')
    
    # Résumé
    print(f"\\n=== RÉSULTATS ===")
    print(f"Logs traités avec succès: {pipeline.processed_count}")
    print(f"Erreurs de parsing: {pipeline.errors_count}")
    print(f"Endpoints analysés: {len(final_stats)}")
    
    for endpoint, stat in final_stats.items():
        print(f"\\n{endpoint}:")
        print(f"  - Requêtes: {stat['total_requests']}")
        print(f"  - Temps moyen: {stat['avg_response_time']:.3f}s")
        print(f"  - Taux d'erreur: {stat['error_rate']:.1f}%")

if __name__ == "__main__":
    demo_pipeline()
    
    # Démonstration stream infini (arrêter avec Ctrl+C)
    print("\\n=== STREAM INFINI (Ctrl+C pour arrêter) ===")
    try:
        stream = infinite_data_stream()
        windowed = process_stream_with_window(stream, window_size=5)
        
        for i, result in enumerate(windowed):
            print(f"Fenêtre {i+1}: Moyenne={result['window_avg']:.1f}, Catégories={result['categories_count']}")
            if i >= 10:  # Limiter pour la démo
                break
                
    except KeyboardInterrupt:
        print("\\nStream arrêté par l'utilisateur.")''',
                    'exercice': '''## 🎯 Exercice Expert : Système de monitoring en temps réel

**Objectif :** Créer un système de monitoring utilisant des générateurs pour analyser des métriques système en temps réel

### 1. Architecture du système

**Structure des données :**
```python
@dataclass
class SystemMetric:
    timestamp: datetime
    metric_type: str  # 'cpu', 'memory', 'disk', 'network'
    value: float
    unit: str
    hostname: str
    additional_info: dict = None
```

### 2. Générateurs à implémenter

**a) Générateur de métriques système**
```python
def system_metrics_generator(interval: float = 1.0) -> Generator[SystemMetric, None, None]:
    """
    Générateur infini qui collecte les métriques système
    Utilise psutil ou simule les données
    """
    pass

def cpu_metrics() -> Generator[SystemMetric, None, None]:
    """Métriques CPU en temps réel"""
    pass

def memory_metrics() -> Generator[SystemMetric, None, None]:
    """Métriques mémoire en temps réel"""
    pass

def disk_metrics() -> Generator[SystemMetric, None, None]:
    """Métriques disque en temps réel"""
    pass
```

**b) Pipeline de traitement**
```python
def anomaly_detector(metrics: Generator[SystemMetric, None, None], 
                    thresholds: dict) -> Generator[SystemMetric, None, None]:
    """
    Détecte les anomalies basées sur des seuils
    thresholds = {'cpu': 80.0, 'memory': 85.0, 'disk': 90.0}
    """
    pass

def sliding_window_average(metrics: Generator[SystemMetric, None, None], 
                         window_size: int = 10) -> Generator[dict, None, None]:
    """
    Calcule la moyenne mobile sur une fenêtre glissante
    """
    pass

def metric_aggregator(metrics: Generator[SystemMetric, None, None],
                     time_window: int = 60) -> Generator[dict, None, None]:
    """
    Agrège les métriques par fenêtre de temps
    """
    pass
```

**c) Système d'alertes**
```python
def alert_generator(anomalies: Generator[SystemMetric, None, None]) -> Generator[dict, None, None]:
    """
    Génère des alertes basées sur les anomalies détectées
    """
    pass

def rate_limited_alerts(alerts: Generator[dict, None, None], 
                       max_alerts_per_minute: int = 5) -> Generator[dict, None, None]:
    """
    Limite le taux d'alertes pour éviter le spam
    """
    pass
```

### 3. Fonctionnalités avancées

**a) Générateur de métriques historiques**
```python
def historical_data_loader(start_date: datetime, 
                          end_date: datetime,
                          chunk_size: int = 1000) -> Generator[List[SystemMetric], None, None]:
    """
    Charge les données historiques par chunks sans surcharger la mémoire
    """
    pass
```

**b) Générateur de patterns**
```python
def pattern_detector(metrics: Generator[SystemMetric, None, None],
                    pattern_window: int = 100) -> Generator[dict, None, None]:
    """
    Détecte des patterns dans les métriques (pics récurrents, tendances, etc.)
    """
    pass
```

**c) Export de données**
```python
def metrics_to_csv(metrics: Generator[SystemMetric, None, None], 
                  filename: str,
                  batch_size: int = 1000):
    """
    Exporte les métriques vers CSV par batch pour économiser la mémoire
    """
    pass

def metrics_to_influxdb(metrics: Generator[SystemMetric, None, None],
                       connection_params: dict):
    """
    Envoie les métriques vers InfluxDB par batch
    """
    pass
```

### 4. Interface de monitoring

```python
class RealTimeMonitor:
    def __init__(self):
        self.active_generators = {}
        self.alert_handlers = []
    
    def start_monitoring(self, metric_types: List[str]):
        """Démarre le monitoring pour les types de métriques spécifiés"""
        pass
    
    def add_alert_handler(self, handler):
        """Ajoute un gestionnaire d'alerte"""
        pass
    
    def get_current_stats(self) -> dict:
        """Retourne les statistiques actuelles"""
        pass
    
    def stop_monitoring(self):
        """Arrête tous les générateurs de monitoring"""
        pass
```

### 5. Exemple d'utilisation

```python
def demo_monitoring():
    """Démonstration du système de monitoring"""
    
    # Configuration
    thresholds = {
        'cpu': 75.0,
        'memory': 80.0,
        'disk': 85.0
    }
    
    # Pipeline complet
    system_gen = system_metrics_generator(interval=0.5)
    anomaly_gen = anomaly_detector(system_gen, thresholds)
    alert_gen = alert_generator(anomaly_gen)
    limited_alerts = rate_limited_alerts(alert_gen, max_alerts_per_minute=3)
    
    # Monitoring en temps réel
    monitor = RealTimeMonitor()
    monitor.start_monitoring(['cpu', 'memory', 'disk'])
    
    try:
        for alert in limited_alerts:
            print(f"🚨 ALERTE: {alert}")
            
            # Sauvegarder l'alerte
            # Envoyer notification
            # Logger l'incident
            
    except KeyboardInterrupt:
        print("Monitoring arrêté")
        monitor.stop_monitoring()
```

### 6. Tests de performance

```python
def benchmark_generators():
    """Compare performance avec/sans générateurs"""
    
    def collect_all_metrics(duration: int) -> List[SystemMetric]:
        """Version sans générateur (charge tout en mémoire)"""
        pass
    
    def process_metrics_stream(duration: int):
        """Version avec générateurs (streaming)"""
        pass
    
    # Comparer utilisation mémoire et performance
```

### 7. Bonus : Machine Learning

```python
def ml_anomaly_detector(metrics: Generator[SystemMetric, None, None],
                       model_path: str) -> Generator[dict, None, None]:
    """
    Utilise un modèle ML pour détecter des anomalies complexes
    """
    pass

def predictive_generator(historical_data: Generator[SystemMetric, None, None],
                        model) -> Generator[SystemMetric, None, None]:
    """
    Prédit les métriques futures basées sur l'historique
    """
    pass
```

### 8. Critères d'évaluation

- **Efficacité mémoire** : Traitement de gros volumes sans épuiser la RAM
- **Performance temps réel** : Latence minimale dans le pipeline
- **Extensibilité** : Facilité d'ajouter de nouveaux types de métriques
- **Robustesse** : Gestion des erreurs et récupération
- **Modularité** : Générateurs réutilisables et composables

Cet exercice teste votre maîtrise des générateurs pour des applications en temps réel !'''
                }
            )
        
        self.stdout.write(
            self.style.SUCCESS('Tous les cours Python ont été créés avec succès !')
        )