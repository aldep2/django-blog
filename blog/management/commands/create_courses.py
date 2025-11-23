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
        
        self.stdout.write(
            self.style.SUCCESS('Tous les cours Python ont été créés avec succès !')
        )