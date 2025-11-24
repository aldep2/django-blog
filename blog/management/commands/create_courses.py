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
        
        # Cours 3: Python Avancé - PARTIE 1
        cours_avance, created = Cours.objects.get_or_create(
            slug='python-avance',
            defaults={
                'titre': 'Python Avancé',
                'description': 'Maîtrisez les concepts avancés de Python : programmation orientée objet, gestion des erreurs, modules et packages.',
                'niveau': 'avance',
                'duree_estimee': 15,
                'ordre': 3,
                'actif': True
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Cours créé: {cours_avance.titre}')
            )
        
        # Chapitre 1: Programmation Orientée Objet - PARTIE 1
        if created or not cours_avance.chapitres.exists():
            Chapitre.objects.get_or_create(
                cours=cours_avance,
                slug='programmation-orientee-objet-1',
                defaults={
                    'titre': 'POO - Classes et Objets',
                    'ordre': 0,
                    'contenu': '''# Programmation Orientée Objet - Classes et Objets

## 🏗️ Qu'est-ce que la POO ?

La **Programmation Orientée Objet** (POO) est un paradigme qui organise le code autour d'**objets** plutôt que de fonctions. Un objet combine des données (attributs) et des comportements (méthodes).

## 📦 Créer votre première classe

```python
class Voiture:
    # Attribut de classe (partagé par toutes les instances)
    nombre_roues = 4
    
    def __init__(self, marque, modele, couleur):
        # Attributs d'instance (propres à chaque objet)
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.kilometrage = 0
        self.moteur_allume = False
    
    def demarrer(self):
        """Démarre le moteur de la voiture"""
        if not self.moteur_allume:
            self.moteur_allume = True
            print(f"La {self.marque} {self.modele} démarre ! 🚗")
        else:
            print("Le moteur est déjà allumé")
    
    def arreter(self):
        """Arrête le moteur"""
        if self.moteur_allume:
            self.moteur_allume = False
            print("Moteur arrêté")
        else:
            print("Le moteur est déjà arrêté")
    
    def rouler(self, distance):
        """Fait rouler la voiture sur une distance donnée"""
        if not self.moteur_allume:
            print("Démarrez d'abord le moteur !")
            return
        
        self.kilometrage += distance
        print(f"Vous avez roulé {distance} km. Kilométrage total: {self.kilometrage} km")

# Créer des objets (instances)
ma_voiture = Voiture("Toyota", "Corolla", "rouge")
voiture_ami = Voiture("BMW", "X5", "noire")

# Utiliser les méthodes
ma_voiture.demarrer()
ma_voiture.rouler(50)
print(f"Ma voiture: {ma_voiture.marque} {ma_voiture.modele} {ma_voiture.couleur}")
```

## 🎯 Méthodes spéciales (dunder methods)

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def __str__(self):
        """Représentation lisible pour l'utilisateur"""
        return f"{self.nom} ({self.age} ans)"
    
    def __repr__(self):
        """Représentation technique pour le développeur"""
        return f"Personne(nom='{self.nom}', age={self.age})"
    
    def __eq__(self, autre):
        """Définit l'égalité entre deux personnes"""
        if isinstance(autre, Personne):
            return self.nom == autre.nom and self.age == autre.age
        return False
    
    def __lt__(self, autre):
        """Permet de comparer l'âge (moins que)"""
        if isinstance(autre, Personne):
            return self.age < autre.age
        return NotImplemented

# Utilisation
alice = Personne("Alice", 25)
bob = Personne("Bob", 30)

print(alice)        # Alice (25 ans) - utilise __str__
print(repr(alice))  # Personne(nom='Alice', age=25) - utilise __repr__
print(alice == bob) # False - utilise __eq__
print(alice < bob)  # True - utilise __lt__
```

## 🔒 Encapsulation et propriétés

```python
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self._solde = solde_initial  # Attribut "privé" par convention
        self._historique = []
    
    @property
    def solde(self):
        """Getter pour le solde (lecture seule)"""
        return self._solde
    
    def deposer(self, montant):
        """Déposer de l'argent"""
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        
        self._solde += montant
        self._historique.append(f"Dépôt: +{montant}€")
        print(f"Dépôt de {montant}€. Nouveau solde: {self._solde}€")
    
    def retirer(self, montant):
        """Retirer de l'argent"""
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        if montant > self._solde:
            raise ValueError("Solde insuffisant")
        
        self._solde -= montant
        self._historique.append(f"Retrait: -{montant}€")
        print(f"Retrait de {montant}€. Nouveau solde: {self._solde}€")
    
    def afficher_historique(self):
        """Affiche l'historique des transactions"""
        print(f"\\n=== Historique de {self.titulaire} ===")
        for transaction in self._historique:
            print(f"• {transaction}")
        print(f"Solde actuel: {self._solde}€")

# Utilisation
compte = CompteBancaire("Alice Dupont", 1000)
print(f"Solde: {compte.solde}€")  # Utilise le getter

compte.deposer(500)
compte.retirer(200)
compte.afficher_historique()
```

## 📊 Attributs de classe vs d'instance

```python
class Employe:
    # Attributs de classe (partagés)
    entreprise = "TechCorp"
    nb_employes = 0
    
    def __init__(self, nom, poste, salaire):
        # Attributs d'instance (uniques)
        self.nom = nom
        self.poste = poste
        self.salaire = salaire
        
        # Incrémenter le compteur d'employés
        Employe.nb_employes += 1
    
    @classmethod
    def changer_entreprise(cls, nouvelle_entreprise):
        """Méthode de classe pour changer le nom de l'entreprise"""
        cls.entreprise = nouvelle_entreprise
    
    @staticmethod
    def calculer_salaire_annuel(salaire_mensuel):
        """Méthode statique - ne dépend pas de l'instance ou de la classe"""
        return salaire_mensuel * 12
    
    def __del__(self):
        """Destructeur - appelé quand l'objet est supprimé"""
        Employe.nb_employes -= 1
        print(f"{self.nom} a quitté l'entreprise")

# Utilisation
emp1 = Employe("Alice", "Développeuse", 4000)
emp2 = Employe("Bob", "Designer", 3500)

print(f"Entreprise: {Employe.entreprise}")
print(f"Nombre d'employés: {Employe.nb_employes}")

# Méthode de classe
Employe.changer_entreprise("NewTech")
print(f"Nouvelle entreprise: {emp1.entreprise}")  # Changé pour tous

# Méthode statique
salaire_annuel = Employe.calculer_salaire_annuel(4000)
print(f"Salaire annuel: {salaire_annuel}€")
```''',
                    'code_exemple': '''# Exemple complet : Système de gestion de bibliothèque avec POO

from datetime import datetime, timedelta

class Livre:
    """Classe représentant un livre dans la bibliothèque"""
    
    def __init__(self, isbn, titre, auteur, annee_publication, genre="Fiction"):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.genre = genre
        self.disponible = True
        self.date_emprunt = None
        self.emprunteur = None
    
    def __str__(self):
        statut = "DISPONIBLE" if self.disponible else f"EMPRUNTÉ par {self.emprunteur}"
        return f"'{self.titre}' par {self.auteur} ({self.annee_publication}) - {statut}"
    
    def __repr__(self):
        return f"Livre(isbn='{self.isbn}', titre='{self.titre}', auteur='{self.auteur}')"
    
    def emprunter(self, nom_emprunteur):
        """Emprunte le livre à une personne"""
        if not self.disponible:
            return False, f"Le livre '{self.titre}' est déjà emprunté"
        
        self.disponible = False
        self.emprunteur = nom_emprunteur
        self.date_emprunt = datetime.now()
        return True, f"Livre '{self.titre}' emprunté par {nom_emprunteur}"
    
    def rendre(self):
        """Rend le livre à la bibliothèque"""
        if self.disponible:
            return False, f"Le livre '{self.titre}' n'est pas emprunté"
        
        emprunteur = self.emprunteur
        self.disponible = True
        self.emprunteur = None
        self.date_emprunt = None
        return True, f"Livre '{self.titre}' rendu par {emprunteur}"
    
    def jours_emprunt(self):
        """Calcule le nombre de jours d'emprunt"""
        if self.disponible or not self.date_emprunt:
            return 0
        return (datetime.now() - self.date_emprunt).days

class Bibliotheque:
    """Classe gérant une collection de livres"""
    
    def __init__(self, nom):
        self.nom = nom
        self.livres = {}  # Dictionnaire {isbn: Livre}
        self.historique_emprunts = []
    
    def ajouter_livre(self, livre):
        """Ajoute un livre à la bibliothèque"""
        if livre.isbn in self.livres:
            return False, f"Un livre avec l'ISBN {livre.isbn} existe déjà"
        
        self.livres[livre.isbn] = livre
        return True, f"Livre '{livre.titre}' ajouté à la bibliothèque"
    
    def supprimer_livre(self, isbn):
        """Supprime un livre de la bibliothèque"""
        if isbn not in self.livres:
            return False, "Livre non trouvé"
        
        livre = self.livres[isbn]
        if not livre.disponible:
            return False, f"Impossible de supprimer '{livre.titre}' : livre emprunté"
        
        del self.livres[isbn]
        return True, f"Livre '{livre.titre}' supprimé"
    
    def rechercher_par_titre(self, titre_partiel):
        """Recherche des livres par titre (recherche partielle)"""
        resultats = []
        titre_lower = titre_partiel.lower()
        
        for livre in self.livres.values():
            if titre_lower in livre.titre.lower():
                resultats.append(livre)
        
        return resultats
    
    def rechercher_par_auteur(self, auteur_partiel):
        """Recherche des livres par auteur"""
        resultats = []
        auteur_lower = auteur_partiel.lower()
        
        for livre in self.livres.values():
            if auteur_lower in livre.auteur.lower():
                resultats.append(livre)
        
        return resultats
    
    def livres_disponibles(self):
        """Retourne la liste des livres disponibles"""
        return [livre for livre in self.livres.values() if livre.disponible]
    
    def livres_empruntes(self):
        """Retourne la liste des livres empruntés"""
        return [livre for livre in self.livres.values() if not livre.disponible]
    
    def emprunter_livre(self, isbn, nom_emprunteur):
        """Emprunte un livre par son ISBN"""
        if isbn not in self.livres:
            return False, "Livre non trouvé"
        
        livre = self.livres[isbn]
        succes, message = livre.emprunter(nom_emprunteur)
        
        if succes:
            self.historique_emprunts.append({
                'action': 'emprunt',
                'livre': livre.titre,
                'emprunteur': nom_emprunteur,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M")
            })
        
        return succes, message
    
    def rendre_livre(self, isbn):
        """Rend un livre par son ISBN"""
        if isbn not in self.livres:
            return False, "Livre non trouvé"
        
        livre = self.livres[isbn]
        succes, message = livre.rendre()
        
        if succes:
            self.historique_emprunts.append({
                'action': 'retour',
                'livre': livre.titre,
                'emprunteur': livre.emprunteur or 'Inconnu',
                'date': datetime.now().strftime("%Y-%m-%d %H:%M")
            })
        
        return succes, message
    
    def statistiques(self):
        """Affiche les statistiques de la bibliothèque"""
        total_livres = len(self.livres)
        disponibles = len(self.livres_disponibles())
        empruntes = len(self.livres_empruntes())
        
        print(f"\\n=== Statistiques de {self.nom} ===")
        print(f"Total de livres: {total_livres}")
        print(f"Disponibles: {disponibles}")
        print(f"Empruntés: {empruntes}")
        print(f"Taux d'emprunt: {(empruntes/total_livres*100) if total_livres > 0 else 0:.1f}%")
        
        # Top genres
        genres = {}
        for livre in self.livres.values():
            genres[livre.genre] = genres.get(livre.genre, 0) + 1
        
        if genres:
            print("\\nGenres les plus populaires:")
            for genre, count in sorted(genres.items(), key=lambda x: x[1], reverse=True)[:3]:
                print(f"  {genre}: {count} livre(s)")
    
    def afficher_tous_livres(self):
        """Affiche tous les livres de la bibliothèque"""
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
            return
        
        print(f"\\n=== Livres de {self.nom} ===")
        for i, livre in enumerate(self.livres.values(), 1):
            print(f"{i}. {livre}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une bibliothèque
    biblio = Bibliotheque("Bibliothèque Municipale")
    
    # Ajouter des livres
    livre1 = Livre("978-2-07-036822-1", "Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "Classique")
    livre2 = Livre("978-2-07-037065-1", "1984", "George Orwell", 1949, "Science-Fiction")
    livre3 = Livre("978-2-253-00203-5", "Les Misérables", "Victor Hugo", 1862, "Classique")
    
    for livre in [livre1, livre2, livre3]:
        succes, message = biblio.ajouter_livre(livre)
        print(message)
    
    # Afficher tous les livres
    biblio.afficher_tous_livres()
    
    # Emprunter un livre
    succes, message = biblio.emprunter_livre("978-2-07-036822-1", "Alice Dupont")
    print(f"\\n{message}")
    
    # Afficher les statistiques
    biblio.statistiques()
    
    # Rechercher des livres
    print("\\n=== Recherche 'Victor' ===")
    resultats = biblio.rechercher_par_auteur("Victor")
    for livre in resultats:
        print(f"• {livre}")''',
                    'exercice': '''## 🎯 Exercice : Système de gestion d'école

**Objectif :** Créer un système complet de gestion d'école avec POO

### Partie 1 : Classes de base

Créez les classes suivantes :

#### 1. Classe `Personne` (classe parent)
```python
class Personne:
    def __init__(self, nom, prenom, age, email):
        # Attributs de base
        pass
    
    def se_presenter(self):
        # Méthode générale de présentation
        pass
```

#### 2. Classe `Etudiant` (hérite de Personne)
```python
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, email, numero_etudiant, classe):
        # Appeler le constructeur parent
        # Ajouter attributs spécifiques : notes, absences
        pass
    
    def ajouter_note(self, matiere, note):
        # Ajouter une note dans une matière
        pass
    
    def calculer_moyenne(self):
        # Calculer la moyenne générale
        pass
    
    def marquer_absent(self, date):
        # Marquer une absence
        pass
```

**Conseils :**
- Utilisez l'héritage pour éviter la duplication
- Implémentez les propriétés avec `@property`
- Gérez les erreurs (étudiant inexistant, note invalide)
- Documentez vos classes avec des docstrings'''
                }
            )
            
            # Chapitre 2: Héritage et Polymorphisme
            Chapitre.objects.get_or_create(
                cours=cours_avance,
                slug='heritage-polymorphisme',
                defaults={
                    'titre': 'Héritage et Polymorphisme',
                    'ordre': 1,
                    'contenu': '''# Héritage et Polymorphisme

## 🧬 L'Héritage - Concept de base

L'**héritage** permet à une classe d'hériter des attributs et méthodes d'une autre classe. La classe qui hérite s'appelle **classe fille** ou **sous-classe**, et celle dont elle hérite est la **classe mère** ou **super-classe**.

## 📚 Héritage simple

```python
# Classe parent (ou classe mère)
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.energie = 100
    
    def manger(self, quantite):
        self.energie += quantite
        print(f"{self.nom} mange et récupère {quantite} d'énergie")
    
    def dormir(self, heures):
        self.energie += heures * 10
        print(f"{self.nom} dort {heures}h et récupère de l'énergie")
    
    def se_presenter(self):
        print(f"Je suis {self.nom}, j'ai {self.age} ans")

# Classe enfant (ou classe fille)
class Chien(Animal):  # Chien hérite d'Animal
    def __init__(self, nom, age, race):
        super().__init__(nom, age)  # Appel du constructeur parent
        self.race = race
        self.dresse = False
    
    def aboyer(self):
        print(f"{self.nom} fait: Woof woof!")
        self.energie -= 5
    
    def rapporter_balle(self):
        if self.dresse:
            print(f"{self.nom} rapporte la balle!")
            self.energie -= 15
        else:
            print(f"{self.nom} ne sait pas encore rapporter la balle")
    
    # Redéfinir une méthode du parent (override)
    def se_presenter(self):
        super().se_presenter()  # Appeler la méthode du parent
        print(f"Je suis un {self.race}")

class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur
        self.griffes_sorties = False
    
    def miauler(self):
        print(f"{self.nom} fait: Miaou!")
        self.energie -= 3
    
    def griffer(self):
        if self.griffes_sorties:
            print(f"{self.nom} griffe avec ses griffes!")
            self.energie -= 10
        else:
            print(f"{self.nom} sort ses griffes d'abord")
            self.griffes_sorties = True

# Utilisation
rex = Chien("Rex", 3, "Labrador")
felix = Chat("Félix", 2, "noir")

# Méthodes héritées
rex.manger(20)
felix.dormir(2)

# Méthodes spécifiques
rex.aboyer()
felix.miauler()

# Méthode redéfinie
rex.se_presenter()
```

## 🎭 Polymorphisme

Le **polymorphisme** permet d'utiliser une même interface (méthode) avec des objets de classes différentes, chacun ayant sa propre implémentation.

```python
class Forme:
    def __init__(self, couleur):
        self.couleur = couleur
    
    def calculer_aire(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")
    
    def afficher_info(self):
        aire = self.calculer_aire()
        print(f"Forme {self.couleur} - Aire: {aire}")

class Rectangle(Forme):
    def __init__(self, couleur, longueur, largeur):
        super().__init__(couleur)
        self.longueur = longueur
        self.largeur = largeur
    
    def calculer_aire(self):
        return self.longueur * self.largeur

class Cercle(Forme):
    def __init__(self, couleur, rayon):
        super().__init__(couleur)
        self.rayon = rayon
    
    def calculer_aire(self):
        return 3.14159 * self.rayon ** 2

class Triangle(Forme):
    def __init__(self, couleur, base, hauteur):
        super().__init__(couleur)
        self.base = base
        self.hauteur = hauteur
    
    def calculer_aire(self):
        return (self.base * self.hauteur) / 2

# Polymorphisme en action !
formes = [
    Rectangle("rouge", 5, 3),
    Cercle("bleu", 4),
    Triangle("vert", 6, 8)
]

# Même méthode, comportement différent selon l'objet
for forme in formes:
    forme.afficher_info()  # Polymorphisme !

# Sortie:
# Forme rouge - Aire: 15
# Forme bleu - Aire: 50.26544
# Forme vert - Aire: 24.0
```

## 🏗️ Héritage multiple

Python permet l'héritage multiple (hériter de plusieurs classes) :

```python
class Voleur:
    def __init__(self):
        self.discretion = 50
        self.vitesse = 30
    
    def voler(self):
        print("Vol discret dans l'ombre...")
        return self.discretion

class Guerrier:
    def __init__(self):
        self.force = 80
        self.defense = 60
    
    def attaquer(self):
        print("Attaque puissante!")
        return self.force

class Assassin(Voleur, Guerrier):  # Héritage multiple
    def __init__(self, nom):
        super().__init__()  # Appelle le premier parent (Voleur)
        Guerrier.__init__(self)  # Appel explicite du second parent
        self.nom = nom
        self.stealth_attack = True
    
    def attaque_sournoise(self):
        if self.stealth_attack:
            degats = self.voler() + self.attaquer()
            print(f"{self.nom} fait une attaque sournoise! Dégâts: {degats}")
            return degats

# Utilisation
ninja = Assassin("Kage")
ninja.attaque_sournoise()
```

## 🔍 Méthodes de classe et statiques dans l'héritage

```python
class Vehicule:
    nombre_vehicules = 0
    
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        Vehicule.nombre_vehicules += 1
    
    @classmethod
    def get_nombre_vehicules(cls):
        return cls.nombre_vehicules
    
    @staticmethod
    def convertir_kmh_ms(vitesse_kmh):
        return vitesse_kmh / 3.6

class Voiture(Vehicule):
    nombre_voitures = 0
    
    def __init__(self, marque, modele, nb_portes):
        super().__init__(marque, modele)
        self.nb_portes = nb_portes
        Voiture.nombre_voitures += 1
    
    @classmethod
    def get_nombre_voitures(cls):
        return cls.nombre_voitures

# Test
v1 = Vehicule("Generic", "Model1")
c1 = Voiture("Toyota", "Corolla", 4)
c2 = Voiture("BMW", "X5", 5)

print(f"Total véhicules: {Vehicule.get_nombre_vehicules()}")  # 3
print(f"Total voitures: {Voiture.get_nombre_voitures()}")    # 2

# Méthode statique accessible depuis toutes les classes
print(f"100 km/h = {Voiture.convertir_kmh_ms(100)} m/s")
```

## 🎯 Propriétés et héritage

```python
class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age
    
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, valeur):
        if isinstance(valeur, str) and valeur.strip():
            self._nom = valeur.strip()
        else:
            raise ValueError("Le nom doit être une chaîne non vide")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, valeur):
        if isinstance(valeur, int) and 0 <= valeur <= 120:
            self._age = valeur
        else:
            raise ValueError("L'âge doit être entre 0 et 120")

class Employe(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self._salaire = salaire
    
    @property
    def salaire(self):
        return self._salaire
    
    @salaire.setter
    def salaire(self, valeur):
        if isinstance(valeur, (int, float)) and valeur >= 0:
            self._salaire = valeur
        else:
            raise ValueError("Le salaire doit être positif")
    
    @property
    def salaire_annuel(self):
        return self._salaire * 12

# Utilisation avec validation automatique
emp = Employe("Alice Dupont", 30, 3500)
print(f"Salaire annuel: {emp.salaire_annuel}€")

# Les setters héritées fonctionnent toujours
emp.age = 31  # Validation automatique
emp.salaire = 3800  # Validation automatique
```

## 🧪 Abstract Base Classes (ABC)

Les classes abstraites définissent une interface que les sous-classes doivent implémenter :

```python
from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, nom):
        self.nom = nom
    
    @abstractmethod
    def jouer(self):
        """Méthode abstraite - doit être implémentée"""
        pass
    
    @abstractmethod
    def accorder(self):
        """Méthode abstraite - doit être implémentée"""
        pass
    
    def presenter(self):
        """Méthode concrète - peut être utilisée telle quelle"""
        print(f"Ceci est un {self.nom}")

class Piano(Instrument):
    def jouer(self):
        print("♪ Joue une mélodie au piano ♪")
    
    def accorder(self):
        print("Accordage des cordes du piano...")

class Guitare(Instrument):
    def __init__(self, nom, nb_cordes=6):
        super().__init__(nom)
        self.nb_cordes = nb_cordes
    
    def jouer(self):
        print("♫ Gratte les cordes de la guitare ♫")
    
    def accorder(self):
        print(f"Accordage des {self.nb_cordes} cordes...")

# Impossible de créer une instance d'Instrument directement
# instrument = Instrument("Test")  # Erreur !

# Mais on peut créer des instances des sous-classes
piano = Piano("Piano à queue")
guitare = Guitare("Guitare classique")

instruments = [piano, guitare]
for instrument in instruments:
    instrument.presenter()
    instrument.accorder()
    instrument.jouer()
    print()
```

## 💡 Bonnes pratiques

1. **Utilisez `super()`** pour appeler les méthodes du parent
2. **Privilégiez la composition à l'héritage** quand c'est approprié
3. **Respectez le principe de substitution de Liskov**
4. **Documentez les contrats des méthodes abstraites**
5. **Évitez l'héritage multiple complexe**

L'héritage et le polymorphisme sont des outils puissants pour créer du code réutilisable et maintenable !''',
                    'code_exemple': '''# Exemple complet : Système de gestion d'employés avec héritage

from abc import ABC, abstractmethod
from datetime import datetime, date

class Personne:
    """Classe de base représentant une personne"""
    
    def __init__(self, nom, prenom, date_naissance, email):
        self._nom = nom
        self._prenom = prenom
        self._date_naissance = date_naissance
        self._email = email
    
    @property
    def nom_complet(self):
        return f"{self._prenom} {self._nom}"
    
    @property
    def age(self):
        today = date.today()
        return today.year - self._date_naissance.year - (
            (today.month, today.day) < (self._date_naissance.month, self._date_naissance.day)
        )
    
    def se_presenter(self):
        return f"Je suis {self.nom_complet}, {self.age} ans"
    
    def __str__(self):
        return f"{self.nom_complet} ({self.age} ans)"

class Employe(Personne, ABC):
    """Classe abstraite pour tous les employés"""
    
    def __init__(self, nom, prenom, date_naissance, email, numero_employe, date_embauche):
        super().__init__(nom, prenom, date_naissance, email)
        self.numero_employe = numero_employe
        self.date_embauche = date_embauche
        self.actif = True
    
    @property
    def anciennete(self):
        """Calcule l'ancienneté en années"""
        today = date.today()
        return today.year - self.date_embauche.year
    
    @abstractmethod
    def calculer_salaire(self):
        """Méthode abstraite pour calculer le salaire"""
        pass
    
    @abstractmethod
    def description_poste(self):
        """Méthode abstraite pour décrire le poste"""
        pass
    
    def se_presenter(self):
        base = super().se_presenter()
        return f"{base}, {self.description_poste()}, {self.anciennete} ans d'ancienneté"

class EmployeTempsPlein(Employe):
    """Employé à temps plein avec salaire fixe"""
    
    def __init__(self, nom, prenom, date_naissance, email, numero_employe, 
                 date_embauche, salaire_mensuel, poste):
        super().__init__(nom, prenom, date_naissance, email, numero_employe, date_embauche)
        self.salaire_mensuel = salaire_mensuel
        self.poste = poste
        self.conges_pris = 0
        self.conges_autorises = 25  # 25 jours par an
    
    def calculer_salaire(self):
        return self.salaire_mensuel
    
    def description_poste(self):
        return f"{self.poste} à temps plein"
    
    def prendre_conges(self, jours):
        if self.conges_pris + jours <= self.conges_autorises:
            self.conges_pris += jours
            return True, f"Congés accordés. Restant: {self.conges_autorises - self.conges_pris} jours"
        return False, "Pas assez de jours de congés disponibles"

class EmployeTempsPartiel(Employe):
    """Employé à temps partiel avec salaire horaire"""
    
    def __init__(self, nom, prenom, date_naissance, email, numero_employe, 
                 date_embauche, salaire_horaire, heures_semaine):
        super().__init__(nom, prenom, date_naissance, email, numero_employe, date_embauche)
        self.salaire_horaire = salaire_horaire
        self.heures_semaine = heures_semaine
        self.heures_travaillees_mois = 0
    
    def calculer_salaire(self):
        # Calcul basé sur les heures travaillées ce mois
        return self.heures_travaillees_mois * self.salaire_horaire
    
    def description_poste(self):
        return f"Temps partiel ({self.heures_semaine}h/semaine)"
    
    def enregistrer_heures(self, heures):
        self.heures_travaillees_mois += heures
        print(f"Heures enregistrées: +{heures}h (Total: {self.heures_travaillees_mois}h)")

class Freelance(Personne):
    """Freelance - hérite de Personne mais pas d'Employe"""
    
    def __init__(self, nom, prenom, date_naissance, email, specialite, taux_horaire):
        super().__init__(nom, prenom, date_naissance, email)
        self.specialite = specialite
        self.taux_horaire = taux_horaire
        self.projets_actifs = []
        self.heures_facturees = 0
    
    def ajouter_projet(self, nom_projet, heures_estimees):
        projet = {
            'nom': nom_projet,
            'heures_estimees': heures_estimees,
            'heures_travaillees': 0,
            'date_debut': datetime.now()
        }
        self.projets_actifs.append(projet)
        return f"Projet '{nom_projet}' ajouté ({heures_estimees}h estimées)"
    
    def facturer_heures(self, nom_projet, heures):
        for projet in self.projets_actifs:
            if projet['nom'] == nom_projet:
                projet['heures_travaillees'] += heures
                self.heures_facturees += heures
                montant = heures * self.taux_horaire
                return f"Facturé: {heures}h sur '{nom_projet}' = {montant}€"
        return "Projet non trouvé"
    
    def revenus_totaux(self):
        return self.heures_facturees * self.taux_horaire
    
    def se_presenter(self):
        base = super().se_presenter()
        return f"{base}, Freelance {self.specialite}"

class Entreprise:
    """Gestionnaire d'entreprise avec polymorphisme"""
    
    def __init__(self, nom):
        self.nom = nom
        self.employes = []
        self.freelances = []
    
    def embaucher_employe(self, employe):
        if isinstance(employe, Employe):
            self.employes.append(employe)
            return f"Employé {employe.nom_complet} embauché"
        return "Seuls les employés peuvent être embauchés"
    
    def engager_freelance(self, freelance):
        if isinstance(freelance, Freelance):
            self.freelances.append(freelance)
            return f"Freelance {freelance.nom_complet} engagé"
        return "Seuls les freelances peuvent être engagés"
    
    def calculer_masse_salariale(self):
        """Polymorphisme en action !"""
        total = 0
        print(f"\\n=== Masse salariale de {self.nom} ===")
        
        for employe in self.employes:
            if employe.actif:
                salaire = employe.calculer_salaire()  # Polymorphisme !
                total += salaire
                print(f"• {employe.nom_complet}: {salaire}€ ({employe.description_poste()})")
        
        print(f"\\nTotal employés: {total}€")
        return total
    
    def afficher_equipe(self):
        """Polymorphisme avec méthode se_presenter"""
        print(f"\\n=== Équipe de {self.nom} ===")
        
        print("EMPLOYÉS:")
        for employe in self.employes:
            if employe.actif:
                print(f"• {employe.se_presenter()}")  # Polymorphisme !
        
        print("\\nFREELANCES:")
        for freelance in self.freelances:
            print(f"• {freelance.se_presenter()}")  # Polymorphisme !

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une entreprise
    entreprise = Entreprise("TechCorp")
    
    # Créer des employés avec différents types
    dev_senior = EmployeTempsPlein(
        "Dupont", "Alice", date(1990, 5, 15), "alice@techcorp.com",
        "E001", date(2020, 3, 1), 4500, "Développeuse Senior"
    )
    
    assistant = EmployeTempsPartiel(
        "Martin", "Bob", date(1995, 8, 20), "bob@techcorp.com",
        "E002", date(2022, 1, 15), 15, 20
    )
    
    designer = Freelance(
        "Dubois", "Clara", date(1988, 12, 3), "clara@design.com",
        "UI/UX Design", 50
    )
    
    # Embaucher/engager
    print(entreprise.embaucher_employe(dev_senior))
    print(entreprise.embaucher_employe(assistant))
    print(entreprise.engager_freelance(designer))
    
    # Simuler du travail
    assistant.enregistrer_heures(80)  # 80h ce mois
    designer.ajouter_projet("Refonte site web", 40)
    print(designer.facturer_heures("Refonte site web", 25))
    
    # Afficher l'équipe (polymorphisme)
    entreprise.afficher_equipe()
    
    # Calculer la masse salariale (polymorphisme)
    entreprise.calculer_masse_salariale()''',
                    'exercice': '''## 🎯 Exercice : Système de gestion de véhicules

**Objectif :** Créer un système de gestion de véhicules utilisant l'héritage et le polymorphisme

### Partie 1 : Classes de base

#### 1. Classe abstraite `Vehicule`
```python
from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        self.kilometrage = 0
    
    @abstractmethod
    def demarrer(self):
        pass
    
    @abstractmethod
    def arreter(self):
        pass
    
    @abstractmethod
    def calculer_consommation(self, distance):
        pass
    
    def vieillir(self):
        # Dépréciation de 10% par an
        age = 2024 - self.annee
        return self.prix * (0.9 ** age)
```

#### 2. Classes spécialisées

**Voiture thermique :**
```python
class VoitureThermique(Vehicule):
    def __init__(self, marque, modele, annee, prix, consommation_100km):
        super().__init__(marque, modele, annee, prix)
        self.consommation_100km = consommation_100km  # L/100km
        self.reservoir = 50  # Litres
        self.moteur_allume = False
    
    def faire_le_plein(self, litres):
        # Ajouter du carburant
        pass
    
    def demarrer(self):
        # Implémenter le démarrage
        pass
```

**Voiture électrique :**
```python
class VoitureElectrique(Vehicule):
    def __init__(self, marque, modele, annee, prix, autonomie_km):
        super().__init__(marque, modele, annee, prix)
        self.autonomie_km = autonomie_km
        self.batterie_pourcentage = 100
        self.en_marche = False
    
    def recharger(self, heures):
        # Recharger la batterie
        pass
    
    def demarrer(self):
        # Implémenter le démarrage électrique
        pass
```

**Moto :**
```python
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, cylindree):
        super().__init__(marque, modele, annee, prix)
        self.cylindree = cylindree
        self.consommation_100km = 4.5  # Consommation fixe
        # Ajouter d'autres attributs spécifiques
```

### Partie 2 : Gestionnaire de parc

#### 3. Classe `ParcVehicules`
```python
class ParcVehicules:
    def __init__(self, nom):
        self.nom = nom
        self.vehicules = []
    
    def ajouter_vehicule(self, vehicule):
        # Ajouter un véhicule au parc
        pass
    
    def demarrer_tous(self):
        # Démarrer tous les véhicules (polymorphisme !)
        pass
    
    def calculer_valeur_totale(self):
        # Calculer la valeur dépréciée de tous les véhicules
        pass
    
    def vehicules_par_type(self):
        # Grouper les véhicules par type
        pass
    
    def simulation_trajet(self, distance_km):
        # Simuler un trajet pour tous les véhicules
        pass
```

### Exemple d'utilisation attendue :

```python
# Créer le parc
parc = ParcVehicules("Parc Municipal")

# Créer différents véhicules
voiture1 = VoitureThermique("Peugeot", "208", 2020, 18000, 5.2)
voiture2 = VoitureElectrique("Tesla", "Model 3", 2022, 45000, 500)
moto1 = Moto("Yamaha", "R1", 2019, 12000, 998)

# Ajouter au parc
parc.ajouter_vehicule(voiture1)
parc.ajouter_vehicule(voiture2)
parc.ajouter_vehicule(moto1)

# Polymorphisme en action
parc.demarrer_tous()  # Chaque véhicule démarre différemment
parc.simulation_trajet(100)  # Consommation différente pour chaque type

print(f"Valeur totale: {parc.calculer_valeur_totale()}€")
```

### Fonctionnalités bonus :

1. **Méthodes spéciales** : `__str__`, `__repr__`, `__eq__` pour comparer
2. **Propriétés calculées** : `@property` pour autonomie restante, âge, etc.
3. **Validation** : Vérifier les valeurs (prix positif, année valide)
4. **Statistiques avancées** : véhicule le plus cher, plus ancien, etc.
5. **Sérialisation JSON** : Sauvegarder/charger le parc
6. **Interface utilisateur** : Menu interactif pour gérer le parc

**Concepts testés :**
- Héritage simple et multiple
- Méthodes abstraites (ABC)
- Polymorphisme
- `super()` et redéfinition de méthodes
- Propriétés et encapsulation

**Sortie attendue :**
```
=== Démarrage de tous les véhicules ===
Peugeot 208: Moteur thermique démarré
Tesla Model 3: Système électrique activé
Yamaha R1: Moteur moto démarré

=== Simulation trajet 100km ===
Peugeot 208: 5.2L consommés
Tesla Model 3: 80% batterie restante
Yamaha R1: 4.5L consommés
```'''
                }
            )
            
            # Chapitre 3: Gestion des Exceptions
            Chapitre.objects.get_or_create(
                cours=cours_avance,
                slug='gestion-exceptions',
                defaults={
                    'titre': 'Gestion des Exceptions',
                    'ordre': 2,
                    'contenu': '''# Gestion des Exceptions en Python

## 🚨 Qu'est-ce qu'une exception ?

Une **exception** est une erreur qui se produit lors de l'exécution d'un programme. Au lieu de faire planter le programme, Python nous permet de "capturer" ces erreurs et de les gérer élégamment.

## 🛡️ Structure try/except de base

```python
try:
    # Code qui peut générer une erreur
    nombre = int(input("Entrez un nombre: "))
    resultat = 10 / nombre
    print(f"Résultat: {resultat}")
except ZeroDivisionError:
    print("Erreur: Division par zéro impossible !")
except ValueError:
    print("Erreur: Vous devez entrer un nombre valide !")

print("Le programme continue normalement...")
```

## 🎯 Capturer plusieurs exceptions

### Méthode 1 : Plusieurs blocs except
```python
def diviser_nombres():
    try:
        a = float(input("Premier nombre: "))
        b = float(input("Deuxième nombre: "))
        resultat = a / b
        print(f"{a} ÷ {b} = {resultat}")
    except ValueError:
        print("❌ Erreur: Entrée invalide - utilisez des nombres")
    except ZeroDivisionError:
        print("❌ Erreur: Division par zéro impossible")
    except KeyboardInterrupt:
        print("\\n❌ Opération annulée par l'utilisateur")

diviser_nombres()
```

### Méthode 2 : Tuple d'exceptions
```python
def operation_securisee():
    try:
        data = eval(input("Entrez une expression: "))  # ⚠️ Dangereux en réalité !
        print(f"Résultat: {data}")
    except (ValueError, SyntaxError, NameError) as e:
        print(f"❌ Erreur de syntaxe ou de valeur: {e}")
    except ZeroDivisionError:
        print("❌ Division par zéro détectée")
    except Exception as e:
        print(f"❌ Erreur inattendue: {type(e).__name__}: {e}")
```

## 🔧 Bloc finally et else

```python
def lire_fichier(nom_fichier):
    fichier = None
    try:
        print(f"📂 Tentative d'ouverture de {nom_fichier}")
        fichier = open(nom_fichier, 'r', encoding='utf-8')
        contenu = fichier.read()
        print(f"✅ Fichier lu avec succès ({len(contenu)} caractères)")
        return contenu
    
    except FileNotFoundError:
        print(f"❌ Fichier '{nom_fichier}' introuvable")
        return None
    
    except PermissionError:
        print(f"❌ Pas de permission pour lire '{nom_fichier}'")
        return None
    
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return None
    
    else:
        # Exécuté seulement si aucune exception n'a été levée
        print("🎉 Lecture réussie sans erreur")
    
    finally:
        # Toujours exécuté, même en cas d'exception
        if fichier and not fichier.closed:
            fichier.close()
            print("🔒 Fichier fermé proprement")

# Test
contenu = lire_fichier("test.txt")
```

## 🎪 Créer ses propres exceptions

```python
# Exception personnalisée simple
class AgeInvalideError(Exception):
    """Exception levée quand un âge est invalide"""
    pass

class EmailInvalideError(Exception):
    """Exception levée quand un email est invalide"""
    def __init__(self, email, message="Email invalide"):
        self.email = email
        self.message = message
        super().__init__(self.message)

class CompteInexistantError(Exception):
    """Exception pour un compte bancaire inexistant"""
    def __init__(self, numero_compte):
        self.numero_compte = numero_compte
        super().__init__(f"Le compte {numero_compte} n'existe pas")

# Utilisation des exceptions personnalisées
class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.set_age(age)
        self.set_email(email)
    
    def set_age(self, age):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise AgeInvalideError(f"Âge invalide: {age}. Doit être entre 0 et 150")
        self.age = age
    
    def set_email(self, email):
        if "@" not in email or "." not in email:
            raise EmailInvalideError(email, f"L'email '{email}' n'est pas valide")
        self.email = email

# Test avec gestion d'erreurs
def creer_personne_securise():
    try:
        nom = input("Nom: ")
        age = int(input("Âge: "))
        email = input("Email: ")
        
        personne = Personne(nom, age, email)
        print(f"✅ Personne créée: {personne.nom} ({personne.age} ans)")
        return personne
        
    except ValueError:
        print("❌ L'âge doit être un nombre entier")
    except AgeInvalideError as e:
        print(f"❌ {e}")
    except EmailInvalideError as e:
        print(f"❌ {e.message}: {e.email}")
    
    return None
```

## 💰 Exemple concret : Système bancaire

```python
class SoldeInsuffisantError(Exception):
    """Exception pour solde insuffisant"""
    def __init__(self, solde_actuel, montant_demande):
        self.solde_actuel = solde_actuel
        self.montant_demande = montant_demande
        super().__init__(
            f"Solde insuffisant: {solde_actuel}€ disponibles, "
            f"{montant_demande}€ demandés"
        )

class CompteBancaire:
    def __init__(self, numero, titulaire, solde_initial=0):
        self.numero = numero
        self.titulaire = titulaire
        self.solde = solde_initial
        self.bloque = False
    
    def retirer(self, montant):
        """Retirer de l'argent avec validation complète"""
        if self.bloque:
            raise Exception("Compte bloqué")
        if montant <= 0:
            raise ValueError("Montant invalide")
        if montant > self.solde:
            raise SoldeInsuffisantError(self.solde, montant)
        
        self.solde -= montant
        print(f"✅ Retrait réussi: {montant}€. Nouveau solde: {self.solde}€")

# Utilisation
compte = CompteBancaire("12345", "Alice", 1000)

try:
    compte.retirer(500)   # ✅ OK
    compte.retirer(600)   # ❌ Solde insuffisant
except SoldeInsuffisantError as e:
    print(f"❌ {e}")
```

## ⚡ Bonnes pratiques

### 1. Spécifiez les exceptions
```python
# ❌ Trop général
try:
    operation_risquee()
except:  # Capture TOUT, même Ctrl+C !
    pass

# ✅ Spécifique
try:
    operation_risquee()
except (ValueError, TypeError) as e:
    handle_error(e)
```

### 2. N'ignorez pas les erreurs
```python
# ❌ Mauvais - erreur silencieuse
try:
    risky_operation()
except Exception:
    pass  # Dangereux !

# ✅ Bon - au minimum logger
try:
    risky_operation()
except Exception as e:
    print(f"Erreur: {e}")
    # Puis décider quoi faire
```

### 3. Utilisez finally pour le nettoyage
```python
# ✅ Ressources toujours libérées
resource = None
try:
    resource = acquire_resource()
    use_resource(resource)
except ResourceError:
    handle_error()
finally:
    if resource:
        release_resource(resource)
```

La gestion d'exceptions permet de créer des programmes robustes et fiables ! 🛡️''',
                    'code_exemple': '''# Exemple complet : Calculatrice robuste avec gestion d'erreurs

class CalculatriceError(Exception):
    """Exception de base pour la calculatrice"""
    pass

class DivisionParZeroError(CalculatriceError):
    """Exception pour division par zéro"""
    def __init__(self):
        super().__init__("Division par zéro impossible")

class OperationInconnueError(CalculatriceError):
    """Exception pour opération non supportée"""
    def __init__(self, operation):
        self.operation = operation
        super().__init__(f"Opération '{operation}' non reconnue")

class NombreInvalideError(CalculatriceError):
    """Exception pour nombre invalide"""
    def __init__(self, valeur):
        self.valeur = valeur
        super().__init__(f"'{valeur}' n'est pas un nombre valide")

class CalculatriceAvancee:
    """Calculatrice avec gestion robuste des erreurs"""
    
    def __init__(self):
        self.historique = []
        self.derniere_reponse = 0
    
    def _valider_nombre(self, valeur):
        """Valide et convertit une valeur en nombre"""
        try:
            if isinstance(valeur, str):
                valeur = valeur.strip()
                if valeur.lower() == 'ans':
                    return self.derniere_reponse
            
            return float(valeur)
        except (ValueError, TypeError):
            raise NombreInvalideError(valeur)
    
    def _enregistrer_operation(self, operation, resultat):
        """Enregistre l'opération dans l'historique"""
        self.historique.append({
            'operation': operation,
            'resultat': resultat,
            'timestamp': __import__('datetime').datetime.now()
        })
        self.derniere_reponse = resultat
    
    def additionner(self, a, b):
        """Addition avec gestion d'erreurs"""
        try:
            a = self._valider_nombre(a)
            b = self._valider_nombre(b)
            resultat = a + b
            
            operation = f"{a} + {b}"
            self._enregistrer_operation(operation, resultat)
            
            print(f"✅ {operation} = {resultat}")
            return resultat
            
        except NombreInvalideError as e:
            print(f"❌ Erreur d'addition: {e}")
            raise
        except Exception as e:
            print(f"❌ Erreur inattendue lors de l'addition: {e}")
            raise CalculatriceError(f"Addition échouée: {e}")
    
    def diviser(self, a, b):
        """Division avec gestion de la division par zéro"""
        try:
            a = self._valider_nombre(a)
            b = self._valider_nombre(b)
            
            if b == 0:
                raise DivisionParZeroError()
            
            resultat = a / b
            operation = f"{a} ÷ {b}"
            self._enregistrer_operation(operation, resultat)
            
            print(f"✅ {operation} = {resultat}")
            return resultat
            
        except DivisionParZeroError:
            print("❌ Impossible de diviser par zéro !")
            raise
        except NombreInvalideError as e:
            print(f"❌ Erreur de division: {e}")
            raise
        except Exception as e:
            print(f"❌ Erreur inattendue lors de la division: {e}")
            raise CalculatriceError(f"Division échouée: {e}")
    
    def puissance(self, base, exposant):
        """Calcul de puissance avec gestion des cas limites"""
        try:
            base = self._valider_nombre(base)
            exposant = self._valider_nombre(exposant)
            
            # Cas spéciaux
            if base == 0 and exposant < 0:
                raise CalculatriceError("0 élevé à une puissance négative")
            
            if abs(base) > 1000 and abs(exposant) > 100:
                raise CalculatriceError("Calcul trop volumineux (risque de débordement)")
            
            resultat = base ** exposant
            
            # Vérifier si le résultat est trop grand
            if abs(resultat) > 10**100:
                raise CalculatriceError("Résultat trop grand pour être affiché")
            
            operation = f"{base} ^ {exposant}"
            self._enregistrer_operation(operation, resultat)
            
            print(f"✅ {operation} = {resultat}")
            return resultat
            
        except NombreInvalideError as e:
            print(f"❌ Erreur de puissance: {e}")
            raise
        except OverflowError:
            error_msg = "Résultat trop grand (débordement numérique)"
            print(f"❌ {error_msg}")
            raise CalculatriceError(error_msg)
        except CalculatriceError:
            raise  # Re-lancer notre exception personnalisée
        except Exception as e:
            print(f"❌ Erreur inattendue lors du calcul de puissance: {e}")
            raise CalculatriceError(f"Calcul de puissance échoué: {e}")
    
    def racine(self, nombre):
        """Racine carrée avec gestion des nombres négatifs"""
        try:
            nombre = self._valider_nombre(nombre)
            
            if nombre < 0:
                raise CalculatriceError("Racine carrée d'un nombre négatif impossible")
            
            resultat = nombre ** 0.5
            operation = f"√{nombre}"
            self._enregistrer_operation(operation, resultat)
            
            print(f"✅ {operation} = {resultat}")
            return resultat
            
        except NombreInvalideError as e:
            print(f"❌ Erreur de racine carrée: {e}")
            raise
        except CalculatriceError:
            raise
        except Exception as e:
            print(f"❌ Erreur inattendue lors du calcul de racine: {e}")
            raise CalculatriceError(f"Calcul de racine échoué: {e}")
    
    def calculer(self, expression):
        """Calcule une expression avec gestion d'erreurs complète"""
        try:
            # Parser simple pour "a op b"
            expression = expression.replace(' ', '')
            
            operators = {'+': self.additionner, '-': lambda a,b: a-b, 
                        '*': lambda a,b: a*b, '/': self.diviser}
            
            for op, func in operators.items():
                if op in expression:
                    parts = expression.split(op, 1)
                    if len(parts) == 2:
                        if func == self.additionner or func == self.diviser:
                            return func(parts[0], parts[1])
                        else:
                            a = self._valider_nombre(parts[0])
                            b = self._valider_nombre(parts[1])
                            if op == '-':
                                resultat = a - b
                                operation = f"{a} - {b}"
                            else:  # multiplication
                                resultat = a * b
                                operation = f"{a} × {b}"
                            
                            self._enregistrer_operation(operation, resultat)
                            print(f"✅ {operation} = {resultat}")
                            return resultat
            
            raise OperationInconnueError(expression)
            
        except (NombreInvalideError, OperationInconnueError, DivisionParZeroError):
            raise
        except Exception as e:
            print(f"❌ Erreur lors du calcul: {e}")
            raise CalculatriceError(f"Calcul échoué: {e}")
    
    def afficher_historique(self):
        """Affiche l'historique des calculs"""
        try:
            if not self.historique:
                print("📋 Historique vide")
                return
            
            print("\\n📋 Historique des calculs:")
            for i, calc in enumerate(self.historique[-10:], 1):  # 10 derniers
                print(f"{i}. {calc['operation']} = {calc['resultat']}")
            
            if len(self.historique) > 10:
                print(f"... et {len(self.historique) - 10} calculs plus anciens")
                
        except Exception as e:
            print(f"❌ Erreur lors de l'affichage de l'historique: {e}")
    
    def effacer_historique(self):
        """Efface l'historique avec confirmation"""
        try:
            if not self.historique:
                print("📋 Historique déjà vide")
                return
            
            nb_calculs = len(self.historique)
            self.historique.clear()
            self.derniere_reponse = 0
            print(f"✅ Historique effacé ({nb_calculs} calculs supprimés)")
            
        except Exception as e:
            print(f"❌ Erreur lors de l'effacement: {e}")

def demo_calculatrice():
    """Démonstration avec différents types d'erreurs"""
    calc = CalculatriceAvancee()
    
    # Tests de différents scénarios
    tests = [
        ("5 + 3", "Addition normale"),
        ("10 / 0", "Division par zéro"),
        ("abc + 5", "Nombre invalide"),
        ("2 ^ 1000", "Puissance trop grande"),
        ("√-4", "Racine négative"),
        ("10 / 2", "Division normale"),
        ("ans + 5", "Utilisation du résultat précédent"),
    ]
    
    for expression, description in tests:
        print(f"\\n--- Test: {description} ---")
        print(f"Expression: {expression}")
        
        try:
            if expression.startswith('√'):
                # Extraction manuelle pour la racine
                nombre = expression[1:]
                calc.racine(nombre)
            else:
                calc.calculer(expression)
                
        except (DivisionParZeroError, NombreInvalideError, 
                OperationInconnueError, CalculatriceError) as e:
            print(f"❌ Erreur gérée: {e}")
        except Exception as e:
            print(f"🚨 Erreur inattendue: {type(e).__name__}: {e}")
    
    # Afficher l'historique final
    calc.afficher_historique()

if __name__ == "__main__":
    demo_calculatrice()''',
                    'exercice': '''## 🎯 Exercice : Système de validation de formulaire

**Objectif :** Créer un système de validation robuste avec exceptions personnalisées

### Partie 1 : Exceptions de validation

Créez une hiérarchie d'exceptions pour différents types d'erreurs de validation :

```python
class ValidationError(Exception):
    """Exception de base pour toutes les erreurs de validation"""
    def __init__(self, field_name, message):
        self.field_name = field_name
        self.message = message
        super().__init__(f"Erreur dans '{field_name}': {message}")

class RequiredFieldError(ValidationError):
    """Exception pour champ obligatoire manquant"""
    def __init__(self, field_name):
        super().__init__(field_name, "Ce champ est obligatoire")

class InvalidEmailError(ValidationError):
    """Exception pour email invalide"""
    pass

class InvalidPhoneError(ValidationError):
    """Exception pour numéro de téléphone invalide"""
    pass

class PasswordTooWeakError(ValidationError):
    """Exception pour mot de passe trop faible"""
    def __init__(self, field_name, requirements):
        self.requirements = requirements
        message = f"Le mot de passe doit contenir: {', '.join(requirements)}"
        super().__init__(field_name, message)

class AgeRangeError(ValidationError):
    """Exception pour âge hors limites"""
    pass

class MultipleValidationError(Exception):
    """Exception pour plusieurs erreurs de validation"""
    def __init__(self, errors):
        self.errors = errors
        super().__init__(f"{len(errors)} erreur(s) de validation")
```

### Partie 2 : Système de validation

```python
import re
from typing import Dict, List, Any, Optional

class FormValidator:
    """Validateur de formulaire avec gestion d'erreurs complète"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_required(self, value: Any, field_name: str):
        """Valide qu'un champ obligatoire n'est pas vide"""
        # À implémenter
        pass
    
    def validate_email(self, email: str, field_name: str):
        """Valide le format d'un email"""
        # À implémenter avec regex
        pass
    
    def validate_phone(self, phone: str, field_name: str):
        """Valide un numéro de téléphone français"""
        # À implémenter (format 0X.XX.XX.XX.XX ou +33.X.XX.XX.XX.XX)
        pass
    
    def validate_password(self, password: str, field_name: str):
        """Valide la force d'un mot de passe"""
        # Critères : min 8 caractères, majuscule, minuscule, chiffre, caractère spécial
        # À implémenter
        pass
    
    def validate_age(self, age: int, field_name: str, min_age: int = 0, max_age: int = 120):
        """Valide un âge dans une fourchette"""
        # À implémenter
        pass
    
    def validate_date(self, date_str: str, field_name: str, date_format: str = "%d/%m/%Y"):
        """Valide et parse une date"""
        # À implémenter avec datetime
        pass
    
    def validate_url(self, url: str, field_name: str):
        """Valide qu'une URL est bien formée"""
        # À implémenter
        pass
    
    def add_error(self, error: ValidationError):
        """Ajoute une erreur à la liste"""
        self.errors.append(error)
    
    def add_warning(self, field_name: str, message: str):
        """Ajoute un avertissement"""
        self.warnings.append({'field': field_name, 'message': message})
    
    def validate_form(self, form_data: Dict[str, Any], rules: Dict[str, Dict]) -> bool:
        """Valide un formulaire complet selon des règles"""
        # Exemple de rules:
        # {
        #     'email': {'required': True, 'type': 'email'},
        #     'age': {'required': True, 'type': 'age', 'min': 18, 'max': 65},
        #     'password': {'required': True, 'type': 'password'},
        #     'phone': {'required': False, 'type': 'phone'}
        # }
        # À implémenter
        pass
    
    def get_errors(self) -> List[ValidationError]:
        """Retourne la liste des erreurs"""
        return self.errors
    
    def get_warnings(self) -> List[Dict]:
        """Retourne la liste des avertissements"""
        return self.warnings
    
    def has_errors(self) -> bool:
        """Vérifie s'il y a des erreurs"""
        return len(self.errors) > 0
    
    def clear(self):
        """Efface toutes les erreurs et avertissements"""
        self.errors.clear()
        self.warnings.clear()
```

### Partie 3 : Gestionnaire de formulaire d'inscription

```python
class RegistrationForm:
    """Formulaire d'inscription avec validation complète"""
    
    def __init__(self):
        self.validator = FormValidator()
    
    def validate_registration(self, form_data: Dict[str, Any]) -> Dict[str, Any]:
        """Valide un formulaire d'inscription complet"""
        # Règles de validation
        rules = {
            'nom': {'required': True, 'type': 'string', 'min_length': 2},
            'prenom': {'required': True, 'type': 'string', 'min_length': 2},
            'email': {'required': True, 'type': 'email'},
            'password': {'required': True, 'type': 'password'},
            'confirm_password': {'required': True, 'type': 'string'},
            'age': {'required': True, 'type': 'age', 'min': 16, 'max': 99},
            'phone': {'required': False, 'type': 'phone'},
            'website': {'required': False, 'type': 'url'},
            'birth_date': {'required': True, 'type': 'date'},
            'terms_accepted': {'required': True, 'type': 'boolean'}
        }
        
        try:
            self.validator.clear()
            
            # Validation avec les règles
            is_valid = self.validator.validate_form(form_data, rules)
            
            # Validation personnalisée pour la confirmation du mot de passe
            if 'password' in form_data and 'confirm_password' in form_data:
                if form_data['password'] != form_data['confirm_password']:
                    self.validator.add_error(
                        ValidationError('confirm_password', 'Les mots de passe ne correspondent pas')
                    )
            
            # Validation des conditions d'utilisation
            if not form_data.get('terms_accepted', False):
                self.validator.add_error(
                    RequiredFieldError('terms_accepted')
                )
            
            return {
                'valid': not self.validator.has_errors(),
                'errors': [{'field': e.field_name, 'message': e.message} for e in self.validator.get_errors()],
                'warnings': self.validator.get_warnings()
            }
            
        except Exception as e:
            # Gestion des erreurs inattendues
            return {
                'valid': False,
                'errors': [{'field': 'system', 'message': f'Erreur système: {e}'}],
                'warnings': []
            }
```

### Exemple d'utilisation :

```python
def test_validation():
    """Test du système de validation avec différents cas"""
    form = RegistrationForm()
    
    # Test cases avec différents types d'erreurs
    test_cases = [
        {
            'name': 'Formulaire valide',
            'data': {
                'nom': 'Dupont',
                'prenom': 'Alice',
                'email': 'alice.dupont@example.com',
                'password': 'MotDePasse123!',
                'confirm_password': 'MotDePasse123!',
                'age': 25,
                'phone': '01.23.45.67.89',
                'birth_date': '15/05/1998',
                'terms_accepted': True
            }
        },
        {
            'name': 'Erreurs multiples',
            'data': {
                'nom': '',  # Manquant
                'email': 'email-invalide',  # Format invalide
                'password': '123',  # Trop faible
                'confirm_password': '456',  # Ne correspond pas
                'age': 15,  # Trop jeune
                'terms_accepted': False  # Non accepté
            }
        }
    ]
    
    for test in test_cases:
        print(f"\\n--- Test: {test['name']} ---")
        result = form.validate_registration(test['data'])
        
        if result['valid']:
            print("✅ Formulaire valide !")
        else:
            print("❌ Erreurs de validation:")
            for error in result['errors']:
                print(f"  • {error['field']}: {error['message']}")
        
        if result['warnings']:
            print("⚠️ Avertissements:")
            for warning in result['warnings']:
                print(f"  • {warning['field']}: {warning['message']}")
```

### Fonctionnalités bonus :

1. **Validation asynchrone** : Vérifier si l'email existe déjà en base
2. **Sanitisation** : Nettoyer les données avant validation
3. **Localisation** : Messages d'erreur en plusieurs langues
4. **Validation conditionnelle** : Règles qui dépendent d'autres champs
5. **Export des erreurs** : JSON, XML pour APIs
6. **Validation en temps réel** : Pour interface utilisateur

### Tests attendus :

```python
def test_edge_cases():
    """Tests des cas limites"""
    validator = FormValidator()
    
    # Test avec None
    # Test avec chaînes vides
    # Test avec caractères spéciaux
    # Test avec très longues chaînes
    # Test avec données malformées
    
    pass
```

**Critères de réussite :**
- Toutes les exceptions personnalisées implémentées
- Validation complète de chaque type de donnée
- Gestion des erreurs multiples
- Messages d'erreur clairs et utiles
- Tests couvrant tous les cas d'erreur
- Performance acceptable (< 100ms pour un formulaire)

**Sortie attendue :**
```
--- Test: Formulaire valide ---
✅ Formulaire valide !

--- Test: Erreurs multiples ---
❌ Erreurs de validation:
  • nom: Ce champ est obligatoire
  • email: Format d'email invalide
  • password: Le mot de passe doit contenir: majuscule, minuscule, chiffre, caractère spécial
  • confirm_password: Les mots de passe ne correspondent pas
  • age: L'âge doit être entre 16 et 99 ans
  • terms_accepted: Ce champ est obligatoire
```'''
                }
            )

            # Chapitre 4: Modules et Packages
            Chapitre.objects.get_or_create(
                cours=cours_avance,
                slug='modules-packages',
                defaults={
                    'titre': 'Modules et Packages',
                    'ordre': 3,
                    'contenu': '''# Modules et Packages Python

## 📦 Qu'est-ce qu'un module ?

Un **module** est un fichier Python (.py) qui contient du code réutilisable : fonctions, classes, variables. Les **packages** sont des dossiers qui regroupent plusieurs modules.

## 🔧 Créer et utiliser un module simple

### Créer un module
Créez un fichier `mathutils.py` :

```python
# mathutils.py
"""Module d'utilitaires mathématiques"""

PI = 3.14159

def calculer_aire_cercle(rayon):
    """Calcule l'aire d'un cercle"""
    return PI * rayon ** 2

def calculer_factorielle(n):
    """Calcule la factorielle de n"""
    if n <= 1:
        return 1
    return n * calculer_factorielle(n - 1)

def est_premier(nombre):
    """Vérifie si un nombre est premier"""
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

class Calculatrice:
    """Classe calculatrice simple"""
    def __init__(self):
        self.historique = []
    
    def additionner(self, a, b):
        resultat = a + b
        self.historique.append(f"{a} + {b} = {resultat}")
        return resultat
```

### Utiliser le module
Dans un autre fichier :

```python
# main.py
import mathutils

# Utiliser les fonctions du module
print(f"Aire du cercle (rayon=5): {mathutils.calculer_aire_cercle(5)}")
print(f"Factorielle de 5: {mathutils.calculer_factorielle(5)}")
print(f"7 est premier: {mathutils.est_premier(7)}")

# Utiliser la classe
calc = mathutils.Calculatrice()
resultat = calc.additionner(10, 20)
print(f"Résultat: {resultat}")
```

## 🎯 Différentes façons d'importer

### 1. Import complet du module
```python
import mathutils

aire = mathutils.calculer_aire_cercle(3)
```

### 2. Import avec alias
```python
import mathutils as math_tools

aire = math_tools.calculer_aire_cercle(3)
```

### 3. Import spécifique
```python
from mathutils import calculer_aire_cercle, PI

aire = calculer_aire_cercle(3)
print(f"Pi = {PI}")
```

### 4. Import avec alias spécifique
```python
from mathutils import calculer_aire_cercle as aire_cercle

aire = aire_cercle(3)
```

### 5. Import de tout (⚠️ à éviter)
```python
from mathutils import *  # Importe tout - peut créer des conflits

aire = calculer_aire_cercle(3)
```

## 📁 Créer un package

Un **package** est un dossier contenant un fichier `__init__.py` :

```
mon_package/
    __init__.py
    module1.py
    module2.py
    sous_package/
        __init__.py
        module3.py
```

### Exemple de package utilitaires

```
utils/
    __init__.py
    fichiers.py
    dates.py
    validation.py
```

**utils/__init__.py** :
```python
"""Package d'utilitaires généraux"""

# Rendre disponibles les fonctions principales
from .fichiers import lire_fichier, ecrire_fichier
from .dates import formater_date, calculer_age
from .validation import valider_email, valider_telephone

# Version du package
__version__ = "1.0.0"

# Ce qui est exporté avec "from utils import *"
__all__ = ['lire_fichier', 'ecrire_fichier', 'formater_date', 
           'calculer_age', 'valider_email', 'valider_telephone']
```

**utils/fichiers.py** :
```python
"""Utilitaires pour la gestion des fichiers"""

import os
from pathlib import Path

def lire_fichier(chemin):
    """Lit un fichier texte de façon sécurisée"""
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Fichier {chemin} introuvable")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture: {e}")
        return None

def ecrire_fichier(chemin, contenu):
    """Écrit dans un fichier avec création du dossier si nécessaire"""
    try:
        # Créer le dossier parent si nécessaire
        Path(chemin).parent.mkdir(parents=True, exist_ok=True)
        
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(contenu)
        return True
    except Exception as e:
        print(f"Erreur lors de l'écriture: {e}")
        return False

def lister_fichiers(dossier, extension=None):
    """Liste les fichiers d'un dossier avec filtrage optionnel"""
    fichiers = []
    try:
        for fichier in os.listdir(dossier):
            chemin_complet = os.path.join(dossier, fichier)
            if os.path.isfile(chemin_complet):
                if extension is None or fichier.endswith(extension):
                    fichiers.append(fichier)
        return fichiers
    except Exception as e:
        print(f"Erreur lors du listage: {e}")
        return []
```

**utils/dates.py** :
```python
"""Utilitaires pour la gestion des dates"""

from datetime import datetime, date, timedelta

def formater_date(date_obj, format_sortie="%d/%m/%Y"):
    """Formate une date selon le format spécifié"""
    if isinstance(date_obj, str):
        # Essayer de parser la date
        try:
            date_obj = datetime.strptime(date_obj, "%Y-%m-%d").date()
        except ValueError:
            return "Date invalide"
    
    return date_obj.strftime(format_sortie)

def calculer_age(date_naissance):
    """Calcule l'âge à partir d'une date de naissance"""
    if isinstance(date_naissance, str):
        try:
            date_naissance = datetime.strptime(date_naissance, "%d/%m/%Y").date()
        except ValueError:
            return None
    
    aujourd_hui = date.today()
    age = aujourd_hui.year - date_naissance.year
    
    # Ajuster si l'anniversaire n'est pas encore passé cette année
    if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
        age -= 1
    
    return age

def ajouter_jours(date_base, nb_jours):
    """Ajoute un nombre de jours à une date"""
    if isinstance(date_base, str):
        date_base = datetime.strptime(date_base, "%d/%m/%Y").date()
    
    return date_base + timedelta(days=nb_jours)
```

### Utiliser le package
```python
# Import du package complet
import utils

contenu = utils.lire_fichier("test.txt")
age = utils.calculer_age("15/05/1990")

# Import spécifique
from utils import lire_fichier, calculer_age
from utils.validation import valider_email

# Import de sous-modules
from utils.dates import formater_date, ajouter_jours
```

## 🌟 Modules de la bibliothèque standard

### os - Système d'exploitation
```python
import os

# Informations sur le système
print(f"Système: {os.name}")
print(f"Dossier courant: {os.getcwd()}")
print(f"Variables d'environnement: {os.environ.get('HOME', 'Non défini')}")

# Manipulation de chemins
chemin = os.path.join("dossier", "fichier.txt")
print(f"Chemin: {chemin}")
print(f"Dossier parent: {os.path.dirname(chemin)}")
print(f"Nom du fichier: {os.path.basename(chemin)}")
```

### datetime - Dates et heures
```python
from datetime import datetime, date, timedelta

# Date et heure actuelles
maintenant = datetime.now()
aujourd_hui = date.today()

print(f"Maintenant: {maintenant}")
print(f"Aujourd'hui: {aujourd_hui}")

# Manipulation des dates
dans_une_semaine = aujourd_hui + timedelta(days=7)
print(f"Dans une semaine: {dans_une_semaine}")

# Formatage
print(f"Format français: {maintenant.strftime('%d/%m/%Y à %H:%M')}")
```

### random - Nombres aléatoires
```python
import random

# Nombre aléatoire
nombre = random.randint(1, 10)
print(f"Nombre aléatoire: {nombre}")

# Choix aléatoire dans une liste
couleurs = ["rouge", "vert", "bleu", "jaune"]
couleur_choisie = random.choice(couleurs)
print(f"Couleur: {couleur_choisie}")

# Mélanger une liste
cartes = list(range(1, 53))
random.shuffle(cartes)
print(f"Cartes mélangées: {cartes[:5]}...")
```

### json - Manipulation JSON
```python
import json

# Données Python vers JSON
data = {
    "nom": "Alice",
    "age": 30,
    "langages": ["Python", "JavaScript", "SQL"]
}

json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(f"JSON:\\n{json_string}")

# JSON vers Python
data_retour = json.loads(json_string)
print(f"Données récupérées: {data_retour}")

# Fichier JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    data_fichier = json.load(f)
```

## 🔍 Introspection de modules

```python
import mathutils

# Voir le contenu d'un module
print(f"Contenu du module: {dir(mathutils)}")

# Documentation
print(f"Documentation: {mathutils.__doc__}")

# Chemin du fichier
print(f"Fichier: {mathutils.__file__}")

# Vérifier si un attribut existe
if hasattr(mathutils, 'PI'):
    print(f"PI = {mathutils.PI}")

# Obtenir un attribut dynamiquement
fonction = getattr(mathutils, 'calculer_aire_cercle', None)
if fonction:
    print(f"Aire: {fonction(5)}")
```

## 📋 if __name__ == "__main__"

```python
# Dans mathutils.py
def fonction_utile():
    return "Je suis une fonction utile"

def tests():
    """Tests du module"""
    print("Test des fonctions...")
    print(f"Aire cercle (r=5): {calculer_aire_cercle(5)}")
    print(f"Factorielle(4): {calculer_factorielle(4)}")

# Ce code s'exécute seulement si le fichier est lancé directement
if __name__ == "__main__":
    print("Module mathutils exécuté directement")
    tests()
else:
    print("Module mathutils importé")
```

## 🛠️ Installer des modules externes

### Avec pip
```bash
# Installer un package
pip install requests

# Installer une version spécifique
pip install Django==4.2

# Installer à partir d'un fichier requirements
pip install -r requirements.txt

# Lister les packages installés
pip list

# Voir les détails d'un package
pip show requests
```

### requirements.txt
```
requests==2.28.1
beautifulsoup4==4.11.1
pandas==1.5.2
matplotlib==3.6.2
```

## 💡 Bonnes pratiques

1. **Organisation claire** : Un module = une responsabilité
2. **Documentation** : Docstrings pour modules, classes et fonctions
3. **Tests** : Utilisez `if __name__ == "__main__"` pour les tests
4. **Imports explicites** : Évitez `from module import *`
5. **Gestion d'erreurs** : Try/except dans les fonctions critiques

Les modules permettent d'organiser et de réutiliser efficacement votre code Python ! 📦''',
                    'code_exemple': '''# Exemple complet : Package de gestion de données

# Structure du package:
# data_manager/
#   __init__.py
#   csv_handler.py
#   json_handler.py
#   validator.py
#   utils.py

# data_manager/__init__.py
"""
Package de gestion de données
Supporte CSV, JSON avec validation
"""

from .csv_handler import CSVManager
from .json_handler import JSONManager
from .validator import DataValidator
from .utils import nettoyer_donnees, statistiques_simples

__version__ = "2.0.0"
__author__ = "Votre Nom"

# Configuration par défaut
DEFAULT_ENCODING = 'utf-8'
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# data_manager/csv_handler.py
import csv
import os
from typing import List, Dict, Any, Optional

class CSVManager:
    """Gestionnaire de fichiers CSV avec validation"""
    
    def __init__(self, encoding='utf-8', delimiter=','):
        self.encoding = encoding
        self.delimiter = delimiter
        self.data = []
        self.headers = []
    
    def lire_csv(self, fichier: str) -> List[Dict[str, Any]]:
        """Lit un fichier CSV et retourne une liste de dictionnaires"""
        try:
            if not os.path.exists(fichier):
                raise FileNotFoundError(f"Fichier {fichier} introuvable")
            
            # Vérifier la taille du fichier
            taille = os.path.getsize(fichier)
            if taille > 50 * 1024 * 1024:  # 50MB
                raise ValueError(f"Fichier trop volumineux: {taille} octets")
            
            with open(fichier, 'r', encoding=self.encoding, newline='') as f:
                # Détecter automatiquement le délimiteur
                sample = f.read(1024)
                f.seek(0)
                
                sniffer = csv.Sniffer()
                if sniffer.has_header(sample):
                    delimiter = sniffer.sniff(sample).delimiter
                else:
                    delimiter = self.delimiter
                
                reader = csv.DictReader(f, delimiter=delimiter)
                self.headers = reader.fieldnames or []
                self.data = list(reader)
                
                print(f"✅ CSV lu: {len(self.data)} lignes, {len(self.headers)} colonnes")
                return self.data
                
        except UnicodeDecodeError:
            print(f"❌ Erreur d'encodage. Essayez avec encoding='latin1'")
            return []
        except Exception as e:
            print(f"❌ Erreur lors de la lecture CSV: {e}")
            return []
    
    def ecrire_csv(self, fichier: str, donnees: List[Dict], 
                   headers: Optional[List[str]] = None) -> bool:
        """Écrit des données dans un fichier CSV"""
        try:
            if not donnees:
                print("⚠️ Aucune donnée à écrire")
                return False
            
            # Utiliser les headers fournis ou déduire des données
            if headers is None:
                headers = list(donnees[0].keys()) if donnees else []
            
            # Créer le dossier parent si nécessaire
            os.makedirs(os.path.dirname(fichier) if os.path.dirname(fichier) else '.', exist_ok=True)
            
            with open(fichier, 'w', encoding=self.encoding, newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers, delimiter=self.delimiter)
                writer.writeheader()
                writer.writerows(donnees)
            
            print(f"✅ CSV écrit: {fichier} ({len(donnees)} lignes)")
            return True
            
        except PermissionError:
            print(f"❌ Pas de permission pour écrire {fichier}")
            return False
        except Exception as e:
            print(f"❌ Erreur lors de l'écriture CSV: {e}")
            return False
    
    def filtrer(self, colonne: str, valeur: Any) -> List[Dict]:
        """Filtre les données selon une colonne et valeur"""
        return [ligne for ligne in self.data if ligne.get(colonne) == str(valeur)]
    
    def trier(self, colonne: str, reverse=False) -> List[Dict]:
        """Trie les données selon une colonne"""
        try:
            return sorted(self.data, key=lambda x: x.get(colonne, ''), reverse=reverse)
        except Exception as e:
            print(f"❌ Erreur lors du tri: {e}")
            return self.data
    
    def statistiques(self) -> Dict[str, Any]:
        """Retourne des statistiques sur les données"""
        if not self.data:
            return {}
        
        stats = {
            'nombre_lignes': len(self.data),
            'nombre_colonnes': len(self.headers),
            'colonnes': self.headers,
            'valeurs_manquantes': {}
        }
        
        # Compter les valeurs manquantes par colonne
        for header in self.headers:
            manquantes = sum(1 for ligne in self.data if not ligne.get(header, '').strip())
            stats['valeurs_manquantes'][header] = manquantes
        
        return stats

# data_manager/json_handler.py
import json
import os
from typing import Dict, List, Any, Union

class JSONManager:
    """Gestionnaire de fichiers JSON avec validation"""
    
    def __init__(self, encoding='utf-8', indent=2):
        self.encoding = encoding
        self.indent = indent
        self.data = None
    
    def lire_json(self, fichier: str) -> Union[Dict, List, None]:
        """Lit un fichier JSON"""
        try:
            if not os.path.exists(fichier):
                raise FileNotFoundError(f"Fichier {fichier} introuvable")
            
            with open(fichier, 'r', encoding=self.encoding) as f:
                self.data = json.load(f)
            
            print(f"✅ JSON lu: {fichier}")
            return self.data
            
        except json.JSONDecodeError as e:
            print(f"❌ Erreur JSON ligne {e.lineno}, colonne {e.colno}: {e.msg}")
            return None
        except Exception as e:
            print(f"❌ Erreur lors de la lecture JSON: {e}")
            return None
    
    def ecrire_json(self, fichier: str, donnees: Union[Dict, List]) -> bool:
        """Écrit des données en format JSON"""
        try:
            # Créer le dossier parent
            os.makedirs(os.path.dirname(fichier) if os.path.dirname(fichier) else '.', exist_ok=True)
            
            with open(fichier, 'w', encoding=self.encoding) as f:
                json.dump(donnees, f, ensure_ascii=False, indent=self.indent)
            
            print(f"✅ JSON écrit: {fichier}")
            return True
            
        except TypeError as e:
            print(f"❌ Données non sérialisables en JSON: {e}")
            return False
        except Exception as e:
            print(f"❌ Erreur lors de l'écriture JSON: {e}")
            return False
    
    def valider_schema(self, schema: Dict) -> bool:
        """Validation basique de schéma JSON"""
        if not self.data:
            return False
        
        # Validation très simple - dans la vraie vie, utilisez jsonschema
        try:
            for cle_requise in schema.get('required', []):
                if cle_requise not in self.data:
                    print(f"❌ Clé manquante: {cle_requise}")
                    return False
            
            for cle, type_attendu in schema.get('properties', {}).items():
                if cle in self.data:
                    if type_attendu == 'string' and not isinstance(self.data[cle], str):
                        print(f"❌ {cle} doit être une chaîne")
                        return False
                    elif type_attendu == 'number' and not isinstance(self.data[cle], (int, float)):
                        print(f"❌ {cle} doit être un nombre")
                        return False
            
            print("✅ Schéma valide")
            return True
            
        except Exception as e:
            print(f"❌ Erreur de validation: {e}")
            return False

# data_manager/utils.py
import re
from typing import List, Dict, Any, Union

def nettoyer_donnees(donnees: List[Dict]) -> List[Dict]:
    """Nettoie les données (espaces, casse, etc.)"""
    donnees_propres = []
    
    for ligne in donnees:
        ligne_propre = {}
        for cle, valeur in ligne.items():
            # Nettoyer la clé
            cle_propre = cle.strip().lower().replace(' ', '_')
            
            # Nettoyer la valeur
            if isinstance(valeur, str):
                valeur_propre = valeur.strip()
                # Convertir en nombre si possible
                try:
                    if '.' in valeur_propre:
                        valeur_propre = float(valeur_propre)
                    else:
                        valeur_propre = int(valeur_propre)
                except ValueError:
                    pass  # Garder comme chaîne
            else:
                valeur_propre = valeur
            
            ligne_propre[cle_propre] = valeur_propre
        
        donnees_propres.append(ligne_propre)
    
    return donnees_propres

def statistiques_simples(donnees: List[Dict], colonne: str) -> Dict[str, Any]:
    """Calcule des statistiques simples sur une colonne"""
    valeurs = []
    for ligne in donnees:
        val = ligne.get(colonne)
        if isinstance(val, (int, float)):
            valeurs.append(val)
    
    if not valeurs:
        return {'erreur': 'Aucune valeur numérique trouvée'}
    
    return {
        'count': len(valeurs),
        'min': min(valeurs),
        'max': max(valeurs),
        'moyenne': sum(valeurs) / len(valeurs),
        'somme': sum(valeurs)
    }

def valider_email(email: str) -> bool:
    """Valide un format d'email simple"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Exemple d'utilisation du package complet
if __name__ == "__main__":
    # Import du package
    from data_manager import CSVManager, JSONManager, nettoyer_donnees, statistiques_simples
    
    print("=== Test du package data_manager ===")
    
    # Test CSV
    csv_manager = CSVManager()
    
    # Créer des données de test
    donnees_test = [
        {'nom': 'Alice', 'age': '25', 'email': 'alice@test.com'},
        {'nom': 'Bob', 'age': '30', 'email': 'bob@test.com'},
        {'nom': ' Charlie ', 'age': '35 ', 'email': 'charlie@test.com'}
    ]
    
    # Écrire et lire CSV
    if csv_manager.ecrire_csv('test_data.csv', donnees_test):
        donnees_lues = csv_manager.lire_csv('test_data.csv')
        print(f"Données lues: {donnees_lues}")
        
        # Nettoyer les données
        donnees_propres = nettoyer_donnees(donnees_lues)
        print(f"Données nettoyées: {donnees_propres}")
        
        # Statistiques
        stats = statistiques_simples(donnees_propres, 'age')
        print(f"Statistiques âge: {stats}")
    
    # Test JSON
    json_manager = JSONManager()
    
    config_test = {
        'application': 'Test App',
        'version': '1.0.0',
        'debug': True,
        'users': donnees_test
    }
    
    if json_manager.ecrire_json('config.json', config_test):
        config_lu = json_manager.lire_json('config.json')
        print(f"Config lue: {config_lu}")''',
                    'exercice': '''## 🎯 Exercice : Package de gestion de blog

**Objectif :** Créer un package complet pour gérer un blog avec modules séparés

### Structure du package à créer :

```
blog_manager/
    __init__.py          # Point d'entrée du package
    models.py            # Classes Article, Utilisateur, Commentaire
    storage.py           # Sauvegarde/chargement (JSON, CSV)
    validator.py         # Validation des données
    formatter.py         # Formatage du contenu (Markdown, HTML)
    statistics.py        # Statistiques du blog
    utils.py             # Utilitaires généraux
```

### Partie 1 : Modèles de données (models.py)

```python
from datetime import datetime
from typing import List, Optional

class Utilisateur:
    def __init__(self, nom: str, email: str, role: str = "lecteur"):
        # À implémenter
        pass
    
    def __str__(self):
        # À implémenter
        pass

class Article:
    def __init__(self, titre: str, contenu: str, auteur: Utilisateur):
        # À implémenter avec:
        # - id unique
        # - date de création
        # - date de modification
        # - tags
        # - statut (brouillon/publié)
        pass
    
    def publier(self):
        # Changer le statut à "publié"
        pass
    
    def ajouter_tag(self, tag: str):
        # Ajouter un tag
        pass

class Commentaire:
    def __init__(self, contenu: str, auteur: Utilisateur, article: Article):
        # À implémenter
        pass

class Blog:
    def __init__(self, nom: str):
        self.nom = nom
        self.articles = []
        self.utilisateurs = []
        self.commentaires = []
    
    def ajouter_article(self, article: Article):
        # À implémenter
        pass
    
    def rechercher_articles(self, terme: str) -> List[Article]:
        # Recherche par titre, contenu ou tags
        pass
    
    def articles_par_auteur(self, auteur: Utilisateur) -> List[Article]:
        # À implémenter
        pass
```

### Partie 2 : Stockage de données (storage.py)

```python
import json
import csv
from typing import Dict, List
from .models import Blog, Article, Utilisateur

class BlogStorage:
    """Gestionnaire de sauvegarde/chargement du blog"""
    
    def __init__(self, fichier_base: str = "blog_data"):
        self.fichier_base = fichier_base
    
    def sauvegarder_json(self, blog: Blog) -> bool:
        """Sauvegarde le blog en format JSON"""
        # À implémenter - convertir les objets en dictionnaires
        pass
    
    def charger_json(self, fichier: str) -> Optional[Blog]:
        """Charge un blog depuis un fichier JSON"""
        # À implémenter - recréer les objets depuis les dictionnaires
        pass
    
    def exporter_csv(self, blog: Blog, fichier: str) -> bool:
        """Exporte les articles en CSV"""
        # À implémenter
        pass
    
    def sauvegarder_backup(self, blog: Blog) -> str:
        """Crée une sauvegarde horodatée"""
        # À implémenter avec timestamp dans le nom de fichier
        pass
```

### Partie 3 : Validation (validator.py)

```python
import re
from typing import List, Tuple

class BlogValidator:
    """Validateur pour les données du blog"""
    
    @staticmethod
    def valider_email(email: str) -> Tuple[bool, str]:
        """Valide un format d'email"""
        # À implémenter avec regex
        pass
    
    @staticmethod
    def valider_article(titre: str, contenu: str) -> List[str]:
        """Valide un article et retourne la liste des erreurs"""
        erreurs = []
        # À implémenter:
        # - titre non vide, max 200 caractères
        # - contenu min 10 caractères
        # - pas de caractères interdits
        return erreurs
    
    @staticmethod
    def nettoyer_contenu(contenu: str) -> str:
        """Nettoie le contenu (HTML, espaces, etc.)"""
        # À implémenter
        pass
    
    @staticmethod
    def detecter_spam(contenu: str) -> bool:
        """Détection simple de spam"""
        # À implémenter avec mots-clés suspects
        pass
```

### Partie 4 : Formatage (formatter.py)

```python
import re
from datetime import datetime

class ContentFormatter:
    """Formatage du contenu pour différents formats"""
    
    @staticmethod
    def markdown_to_html(markdown: str) -> str:
        """Conversion Markdown basique vers HTML"""
        # À implémenter:
        # **gras** -> <strong>gras</strong>
        # *italique* -> <em>italique</em>
        # # Titre -> <h1>Titre</h1>
        # [lien](url) -> <a href="url">lien</a>
        pass
    
    @staticmethod
    def extraire_resume(contenu: str, nb_mots: int = 50) -> str:
        """Extrait un résumé du contenu"""
        # À implémenter
        pass
    
    @staticmethod
    def formatter_date(date: datetime, format_fr: bool = True) -> str:
        """Formate une date en français ou anglais"""
        # À implémenter
        pass
    
    @staticmethod
    def generer_slug(titre: str) -> str:
        """Génère un slug URL-friendly depuis un titre"""
        # À implémenter: "Mon Titre !" -> "mon-titre"
        pass
```

### Partie 5 : Statistiques (statistics.py)

```python
from collections import Counter
from datetime import datetime, timedelta
from .models import Blog

class BlogStatistics:
    """Calculateur de statistiques pour le blog"""
    
    def __init__(self, blog: Blog):
        self.blog = blog
    
    def stats_generales(self) -> dict:
        """Statistiques générales du blog"""
        # À implémenter:
        # - nombre d'articles total
        # - nombre d'articles publiés
        # - nombre d'auteurs
        # - nombre de commentaires
        pass
    
    def articles_par_mois(self) -> dict:
        """Nombre d'articles publiés par mois"""
        # À implémenter
        pass
    
    def tags_populaires(self, limite: int = 10) -> list:
        """Tags les plus utilisés"""
        # À implémenter avec Counter
        pass
    
    def auteurs_prolific(self) -> list:
        """Auteurs les plus productifs"""
        # À implémenter
        pass
    
    def articles_recents(self, nb_jours: int = 7) -> list:
        """Articles publiés dans les X derniers jours"""
        # À implémenter
        pass
```

### Partie 6 : Point d'entrée (__init__.py)

```python
"""
Package de gestion de blog
Permet de créer, gérer et analyser un blog simple
"""

from .models import Blog, Article, Utilisateur, Commentaire
from .storage import BlogStorage
from .validator import BlogValidator
from .formatter import ContentFormatter
from .statistics import BlogStatistics

__version__ = "1.0.0"
__author__ = "Votre Nom"

# Fonctions de convenance
def creer_blog(nom: str) -> Blog:
    """Crée un nouveau blog"""
    return Blog(nom)

def charger_blog(fichier: str) -> Blog:
    """Charge un blog depuis un fichier"""
    storage = BlogStorage()
    return storage.charger_json(fichier)

# Export des classes principales
__all__ = [
    'Blog', 'Article', 'Utilisateur', 'Commentaire',
    'BlogStorage', 'BlogValidator', 'ContentFormatter', 'BlogStatistics',
    'creer_blog', 'charger_blog'
]
```

### Exemple d'utilisation :

```python
from blog_manager import Blog, Article, Utilisateur, BlogStorage, BlogStatistics
from blog_manager.formatter import ContentFormatter

# Créer un blog
mon_blog = Blog("Mon Super Blog")

# Créer des utilisateurs
alice = Utilisateur("Alice", "alice@example.com", "auteur")
bob = Utilisateur("Bob", "bob@example.com", "lecteur")

# Créer des articles
article1 = Article("# Mon premier article", "Contenu **important**", alice)
article1.ajouter_tag("python")
article1.ajouter_tag("tutorial")
article1.publier()

mon_blog.ajouter_article(article1)

# Sauvegarder
storage = BlogStorage()
storage.sauvegarder_json(mon_blog)

# Statistiques
stats = BlogStatistics(mon_blog)
print(stats.stats_generales())

# Formatage
html = ContentFormatter.markdown_to_html(article1.contenu)
print(html)
```

### Tests à implémenter :

1. **Test des modèles** : Création, modification, relations
2. **Test de sauvegarde** : JSON, CSV, backup
3. **Test de validation** : Email, contenu, spam
4. **Test de formatage** : Markdown, slugs, dates
5. **Test des statistiques** : Comptages, classements

**Fonctionnalités bonus :**
- Import depuis d'autres formats (WordPress, etc.)
- Génération de site statique HTML
- API REST pour le blog
- Système de plugins
- Cache intelligent
- Recherche full-text

Ce package devra être modulaire, bien documenté et facilement extensible !'''
                }
            )
            
            # Chapitre 5: Fichiers et Données
            Chapitre.objects.get_or_create(
                cours=cours_avance,
                slug='fichiers-donnees',
                defaults={
                    'titre': 'Fichiers et Données',
                    'ordre': 4,
                    'contenu': '''# Fichiers et Données en Python

## 📁 Gestion des fichiers

### Ouvrir et lire un fichier
```python
# Méthode basique
fichier = open("mon_fichier.txt", "r", encoding="utf-8")
contenu = fichier.read()
fichier.close()

# Méthode recommandée avec 'with' (fermeture automatique)
with open("mon_fichier.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(contenu)
# Le fichier se ferme automatiquement ici
```

### Modes d'ouverture
```python
# 'r' - Lecture seule (défaut)
with open("fichier.txt", "r") as f:
    contenu = f.read()

# 'w' - Écriture (écrase le fichier existant)
with open("fichier.txt", "w") as f:
    f.write("Nouveau contenu")

# 'a' - Ajout (ajoute à la fin du fichier)
with open("fichier.txt", "a") as f:
    f.write("\\nLigne ajoutée")

# 'r+' - Lecture et écriture
with open("fichier.txt", "r+") as f:
    contenu = f.read()
    f.write("Ajout")

# 'b' - Mode binaire (pour images, vidéos, etc.)
with open("image.jpg", "rb") as f:
    donnees_binaires = f.read()
```

### Différentes méthodes de lecture
```python
with open("data.txt", "r", encoding="utf-8") as fichier:
    # Lire tout le fichier
    tout = fichier.read()
    
    # Revenir au début
    fichier.seek(0)
    
    # Lire ligne par ligne
    for ligne in fichier:
        print(ligne.strip())  # strip() enlève le \\n
    
    # Lire toutes les lignes dans une liste
    fichier.seek(0)
    lignes = fichier.readlines()
    
    # Lire une seule ligne
    fichier.seek(0)
    premiere_ligne = fichier.readline()
```

### Écriture de fichiers
```python
# Écrire du texte
with open("sortie.txt", "w", encoding="utf-8") as f:
    f.write("Première ligne\\n")
    f.write("Deuxième ligne\\n")
    
    # Écrire plusieurs lignes
    lignes = ["Ligne 3\\n", "Ligne 4\\n", "Ligne 5\\n"]
    f.writelines(lignes)

# Écrire avec print (redirection)
with open("log.txt", "w") as f:
    print("Message de log", file=f)
    print("Autre message", file=f)
```

## 🗂️ Manipulation de chemins avec pathlib

```python
from pathlib import Path

# Créer un chemin
chemin = Path("dossier/sous_dossier/fichier.txt")

# Informations sur le chemin
print(f"Nom du fichier: {chemin.name}")           # fichier.txt
print(f"Extension: {chemin.suffix}")              # .txt
print(f"Nom sans extension: {chemin.stem}")       # fichier
print(f"Dossier parent: {chemin.parent}")         # dossier/sous_dossier
print(f"Chemin absolu: {chemin.absolute()}")

# Vérifications
print(f"Existe: {chemin.exists()}")
print(f"Est un fichier: {chemin.is_file()}")
print(f"Est un dossier: {chemin.is_dir()}")

# Création de dossiers
nouveau_dossier = Path("projet/data")
nouveau_dossier.mkdir(parents=True, exist_ok=True)  # Crée tous les parents

# Lister le contenu d'un dossier
dossier = Path(".")
for element in dossier.iterdir():
    if element.is_file():
        print(f"Fichier: {element}")
    else:
        print(f"Dossier: {element}")

# Recherche de fichiers
for fichier_py in Path(".").rglob("*.py"):  # Récursif
    print(fichier_py)
```

## 📊 Fichiers CSV

### Lecture de CSV
```python
import csv

# Lecture simple
with open("data.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        print(ligne)  # Chaque ligne est une liste

# Lecture avec headers (DictReader)
with open("data.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        print(ligne)  # Chaque ligne est un dictionnaire
        print(f"Nom: {ligne['nom']}, Age: {ligne['age']}")
```

### Écriture de CSV
```python
import csv

# Écriture simple
donnees = [
    ["nom", "age", "ville"],
    ["Alice", "25", "Paris"],
    ["Bob", "30", "Lyon"],
    ["Charlie", "35", "Marseille"]
]

with open("sortie.csv", "w", newline="", encoding="utf-8") as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerows(donnees)

# Écriture avec DictWriter
donnees_dict = [
    {"nom": "Alice", "age": 25, "ville": "Paris"},
    {"nom": "Bob", "age": 30, "ville": "Lyon"},
    {"nom": "Charlie", "age": 35, "ville": "Marseille"}
]

with open("sortie_dict.csv", "w", newline="", encoding="utf-8") as fichier:
    fieldnames = ["nom", "age", "ville"]
    ecrivain = csv.DictWriter(fichier, fieldnames=fieldnames)
    
    ecrivain.writeheader()  # Écrit les en-têtes
    ecrivain.writerows(donnees_dict)
```

## 🔄 Fichiers JSON

### Lecture JSON
```python
import json

# Depuis un fichier
with open("config.json", "r", encoding="utf-8") as fichier:
    data = json.load(fichier)
    print(data)

# Depuis une chaîne
json_string = '{"nom": "Alice", "age": 25, "langages": ["Python", "JavaScript"]}'
data = json.loads(json_string)
print(data["nom"])  # Alice
```

### Écriture JSON
```python
import json

# Données Python
config = {
    "app_name": "Mon App",
    "version": "1.0.0",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "features": ["auth", "api", "dashboard"]
}

# Vers un fichier
with open("config.json", "w", encoding="utf-8") as fichier:
    json.dump(config, fichier, ensure_ascii=False, indent=2)

# Vers une chaîne
json_string = json.dumps(config, ensure_ascii=False, indent=2)
print(json_string)
```

## 🗃️ Pickle - Sérialisation d'objets Python

```python
import pickle

# Sauvegarder des objets Python
data = {
    "liste": [1, 2, 3, 4, 5],
    "dictionnaire": {"a": 1, "b": 2},
    "tuple": (10, 20, 30)
}

# Écriture
with open("data.pickle", "wb") as fichier:
    pickle.dump(data, fichier)

# Lecture
with open("data.pickle", "rb") as fichier:
    data_chargee = pickle.load(fichier)
    print(data_chargee)

# Sérialisation de classes personnalisées
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def __repr__(self):
        return f"Personne('{self.nom}', {self.age})"

alice = Personne("Alice", 25)

# Sauvegarder l'objet
with open("personne.pickle", "wb") as f:
    pickle.dump(alice, f)

# Charger l'objet
with open("personne.pickle", "rb") as f:
    alice_chargee = pickle.load(f)
    print(alice_chargee)  # Personne('Alice', 25)
```

## 📈 Traitement de données avec des fichiers

### Analyser un fichier de logs
```python
import re
from collections import Counter
from datetime import datetime

def analyser_logs(fichier_log):
    """Analyse un fichier de logs web"""
    ips = []
    status_codes = []
    urls = []
    
    pattern = r'(\\d+\\.\\d+\\.\\d+\\.\\d+) - - \\[(.*?)\\] "GET (.*?) HTTP/1\\.1" (\\d+) (\\d+)'
    
    with open(fichier_log, "r") as f:
        for ligne in f:
            match = re.match(pattern, ligne)
            if match:
                ip, date_str, url, status, size = match.groups()
                ips.append(ip)
                status_codes.append(int(status))
                urls.append(url)
    
    # Statistiques
    print(f"Total de requêtes: {len(ips)}")
    print(f"IPs uniques: {len(set(ips))}")
    print(f"\\nTop 5 IPs:")
    for ip, count in Counter(ips).most_common(5):
        print(f"  {ip}: {count} requêtes")
    
    print(f"\\nCodes de statut:")
    for code, count in Counter(status_codes).most_common():
        print(f"  {code}: {count}")

# Exemple d'utilisation
# analyser_logs("access.log")
```

### Traitement de fichier CSV volumineux
```python
import csv
from collections import defaultdict

def analyser_ventes(fichier_csv):
    """Analyse un fichier de données de ventes"""
    ventes_par_mois = defaultdict(float)
    ventes_par_produit = defaultdict(float)
    total_general = 0
    
    with open(fichier_csv, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        
        for ligne in lecteur:
            date = ligne["date"]
            produit = ligne["produit"] 
            montant = float(ligne["montant"])
            
            # Extraire le mois
            mois = date[:7]  # Format YYYY-MM
            
            ventes_par_mois[mois] += montant
            ventes_par_produit[produit] += montant
            total_general += montant
    
    # Rapport
    print(f"Chiffre d'affaires total: {total_general:.2f}€")
    print(f"\\nVentes par mois:")
    for mois in sorted(ventes_par_mois.keys()):
        print(f"  {mois}: {ventes_par_mois[mois]:.2f}€")
    
    print(f"\\nTop 5 produits:")
    for produit, montant in sorted(ventes_par_produit.items(), 
                                   key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {produit}: {montant:.2f}€")
```

## 🔍 Gestion d'erreurs avec fichiers

```python
import os
import shutil
from pathlib import Path

def copier_fichier_securise(source, destination):
    """Copie un fichier avec gestion d'erreurs complète"""
    try:
        source_path = Path(source)
        dest_path = Path(destination)
        
        # Vérifications
        if not source_path.exists():
            raise FileNotFoundError(f"Fichier source '{source}' introuvable")
        
        if not source_path.is_file():
            raise ValueError(f"'{source}' n'est pas un fichier")
        
        # Créer le dossier de destination si nécessaire
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Vérifier l'espace disque (approximatif)
        taille_source = source_path.stat().st_size
        espace_libre = shutil.disk_usage(dest_path.parent).free
        
        if taille_source > espace_libre:
            raise OSError("Espace disque insuffisant")
        
        # Copier le fichier
        shutil.copy2(source, destination)
        print(f"✅ Fichier copié: {source} -> {destination}")
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Fichier introuvable: {e}")
    except PermissionError as e:
        print(f"❌ Permission refusée: {e}")
    except OSError as e:
        print(f"❌ Erreur système: {e}")
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
    
    return False

def nettoyer_dossier(dossier, extension, jours_anciens=30):
    """Supprime les fichiers anciens d'une extension donnée"""
    import time
    
    try:
        dossier_path = Path(dossier)
        if not dossier_path.exists():
            print(f"Dossier {dossier} n'existe pas")
            return
        
        fichiers_supprimes = 0
        temps_limite = time.time() - (jours_anciens * 24 * 3600)
        
        for fichier in dossier_path.rglob(f"*.{extension}"):
            if fichier.is_file():
                temps_modif = fichier.stat().st_mtime
                if temps_modif < temps_limite:
                    try:
                        fichier.unlink()  # Supprimer
                        fichiers_supprimes += 1
                        print(f"Supprimé: {fichier}")
                    except PermissionError:
                        print(f"Permission refusée: {fichier}")
        
        print(f"✅ {fichiers_supprimes} fichier(s) .{extension} supprimé(s)")
        
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage: {e}")
```

## 💾 Sauvegarde et compression

```python
import zipfile
import tarfile
import shutil
from datetime import datetime

def creer_sauvegarde(dossier_source, dossier_backup):
    """Crée une archive de sauvegarde horodatée"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_archive = f"backup_{timestamp}.zip"
        chemin_archive = Path(dossier_backup) / nom_archive
        
        # Créer le dossier de backup
        Path(dossier_backup).mkdir(parents=True, exist_ok=True)
        
        with zipfile.ZipFile(chemin_archive, 'w', zipfile.ZIP_DEFLATED) as archive:
            for fichier in Path(dossier_source).rglob('*'):
                if fichier.is_file():
                    # Chemin relatif dans l'archive
                    chemin_relatif = fichier.relative_to(dossier_source)
                    archive.write(fichier, chemin_relatif)
        
        taille = chemin_archive.stat().st_size
        print(f"✅ Sauvegarde créée: {nom_archive} ({taille} octets)")
        return str(chemin_archive)
        
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")
        return None

def extraire_archive(archive, destination):
    """Extrait une archive avec gestion d'erreurs"""
    try:
        archive_path = Path(archive)
        dest_path = Path(destination)
        
        dest_path.mkdir(parents=True, exist_ok=True)
        
        if archive_path.suffix == '.zip':
            with zipfile.ZipFile(archive, 'r') as z:
                z.extractall(destination)
        elif archive_path.suffix in ['.tar', '.tar.gz', '.tgz']:
            with tarfile.open(archive, 'r') as t:
                t.extractall(destination)
        else:
            raise ValueError(f"Format d'archive non supporté: {archive_path.suffix}")
        
        print(f"✅ Archive extraite dans: {destination}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'extraction: {e}")
        return False
```

## 📋 Bonnes pratiques

1. **Utilisez toujours `with open()`** pour la fermeture automatique
2. **Spécifiez l'encodage** (`encoding="utf-8"`) pour éviter les problèmes
3. **Gérez les erreurs** avec try/except appropriés
4. **Utilisez `pathlib`** plutôt que les chaînes pour les chemins
5. **Vérifiez l'existence** des fichiers avant manipulation
6. **Libérez les ressources** (fermeture de fichiers, connexions)
7. **Sauvegardez** avant les opérations destructives

La manipulation de fichiers est essentielle pour traiter des données réelles ! 📊''',
                    'code_exemple': '''# Exemple complet : Gestionnaire de journaux avec analyse

import csv
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter, defaultdict
import zipfile

class JournalManager:
    """Gestionnaire complet pour les fichiers de journaux"""
    
    def __init__(self, dossier_logs="logs", dossier_archives="archives"):
        self.dossier_logs = Path(dossier_logs)
        self.dossier_archives = Path(dossier_archives)
        self.dossier_logs.mkdir(exist_ok=True)
        self.dossier_archives.mkdir(exist_ok=True)
        
        # Patterns pour différents types de logs
        self.patterns = {
            'apache': r'(\\S+) \\S+ \\S+ \\[(.*?)\\] "([A-Z]+) (.*?) HTTP/\\d\\.\\d" (\\d+) (\\d+)',
            'custom': r'\\[(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2})\\] (\\w+): (.+)'
        }
    
    def ecrire_log(self, message, niveau="INFO", fichier="app.log"):
        """Écrit un message dans un fichier de log"""
        try:
            chemin_log = self.dossier_logs / fichier
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ligne_log = f"[{timestamp}] {niveau}: {message}\\n"
            
            with open(chemin_log, "a", encoding="utf-8") as f:
                f.write(ligne_log)
            
            return True
            
        except Exception as e:
            print(f"Erreur lors de l'écriture du log: {e}")
            return False
    
    def lire_logs(self, fichier, type_log="custom", limite=None):
        """Lit et parse un fichier de logs"""
        try:
            chemin_log = self.dossier_logs / fichier
            if not chemin_log.exists():
                print(f"Fichier {fichier} introuvable")
                return []
            
            pattern = self.patterns.get(type_log, self.patterns['custom'])
            logs_parses = []
            
            with open(chemin_log, "r", encoding="utf-8") as f:
                lignes = f.readlines()
                if limite:
                    lignes = lignes[-limite:]  # Dernières lignes
                
                for ligne in lignes:
                    match = re.match(pattern, ligne.strip())
                    if match:
                        if type_log == "custom":
                            timestamp, niveau, message = match.groups()
                            logs_parses.append({
                                'timestamp': timestamp,
                                'niveau': niveau,
                                'message': message,
                                'ligne_complete': ligne.strip()
                            })
                        elif type_log == "apache":
                            ip, timestamp, methode, url, status, taille = match.groups()
                            logs_parses.append({
                                'ip': ip,
                                'timestamp': timestamp,
                                'methode': methode,
                                'url': url,
                                'status': int(status),
                                'taille': int(taille) if taille != '-' else 0,
                                'ligne_complete': ligne.strip()
                            })
            
            print(f"✅ {len(logs_parses)} entrées de log parsées")
            return logs_parses
            
        except Exception as e:
            print(f"Erreur lors de la lecture des logs: {e}")
            return []
    
    def analyser_logs(self, fichier, type_log="custom"):
        """Analyse complète d'un fichier de logs"""
        logs = self.lire_logs(fichier, type_log)
        if not logs:
            return None
        
        if type_log == "custom":
            return self._analyser_logs_custom(logs)
        elif type_log == "apache":
            return self._analyser_logs_apache(logs)
    
    def _analyser_logs_custom(self, logs):
        """Analyse spécifique pour les logs custom"""
        niveaux = Counter(log['niveau'] for log in logs)
        
        # Messages par heure
        messages_par_heure = defaultdict(int)
        for log in logs:
            try:
                dt = datetime.strptime(log['timestamp'], "%Y-%m-%d %H:%M:%S")
                heure = dt.strftime("%H:00")
                messages_par_heure[heure] += 1
            except ValueError:
                continue
        
        # Mots les plus fréquents dans les messages
        mots = []
        for log in logs:
            mots.extend(log['message'].lower().split())
        mots_frequents = Counter(mots).most_common(10)
        
        return {
            'total_entrees': len(logs),
            'niveaux': dict(niveaux),
            'messages_par_heure': dict(messages_par_heure),
            'mots_frequents': mots_frequents
        }
    
    def _analyser_logs_apache(self, logs):
        """Analyse spécifique pour les logs Apache"""
        # IPs les plus actives
        ips = Counter(log['ip'] for log in logs)
        
        # Codes de statut
        status_codes = Counter(log['status'] for log in logs)
        
        # URLs les plus demandées
        urls = Counter(log['url'] for log in logs)
        
        # Trafic par heure
        trafic_par_heure = defaultdict(int)
        for log in logs:
            try:
                # Format: 10/Oct/2023:14:55:36 +0000
                timestamp_str = log['timestamp']
                # Extraction simple de l'heure
                if ':' in timestamp_str:
                    heure = timestamp_str.split(':')[1]
                    trafic_par_heure[f"{heure}:00"] += 1
            except (ValueError, IndexError):
                continue
        
        return {
            'total_requetes': len(logs),
            'ips_uniques': len(set(log['ip'] for log in logs)),
            'top_ips': ips.most_common(5),
            'status_codes': dict(status_codes),
            'top_urls': urls.most_common(10),
            'trafic_par_heure': dict(trafic_par_heure)
        }
    
    def exporter_analyse(self, fichier_log, format_sortie="json", type_log="custom"):
        """Exporte l'analyse dans différents formats"""
        try:
            analyse = self.analyser_logs(fichier_log, type_log)
            if not analyse:
                return False
            
            nom_base = Path(fichier_log).stem
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if format_sortie == "json":
                fichier_sortie = f"analyse_{nom_base}_{timestamp}.json"
                chemin_sortie = self.dossier_archives / fichier_sortie
                
                with open(chemin_sortie, "w", encoding="utf-8") as f:
                    json.dump(analyse, f, ensure_ascii=False, indent=2, default=str)
            
            elif format_sortie == "csv":
                fichier_sortie = f"analyse_{nom_base}_{timestamp}.csv"
                chemin_sortie = self.dossier_archives / fichier_sortie
                
                # Conversion en format tabulaire pour CSV
                with open(chemin_sortie, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    
                    # En-têtes et données selon le type d'analyse
                    if 'niveaux' in analyse:  # Logs custom
                        writer.writerow(["Métrique", "Valeur"])
                        writer.writerow(["Total entrées", analyse['total_entrees']])
                        writer.writerow([])
                        writer.writerow(["Niveau", "Nombre"])
                        for niveau, count in analyse['niveaux'].items():
                            writer.writerow([niveau, count])
                    
                    elif 'top_ips' in analyse:  # Logs Apache
                        writer.writerow(["Métrique", "Valeur"])
                        writer.writerow(["Total requêtes", analyse['total_requetes']])
                        writer.writerow(["IPs uniques", analyse['ips_uniques']])
                        writer.writerow([])
                        writer.writerow(["IP", "Requêtes"])
                        for ip, count in analyse['top_ips']:
                            writer.writerow([ip, count])
            
            print(f"✅ Analyse exportée: {fichier_sortie}")
            return str(chemin_sortie)
            
        except Exception as e:
            print(f"❌ Erreur lors de l'export: {e}")
            return None
    
    def archiver_logs_anciens(self, jours_anciens=7):
        """Archive les logs de plus de X jours"""
        try:
            date_limite = datetime.now() - timedelta(days=jours_anciens)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_archive = f"logs_archive_{timestamp}.zip"
            chemin_archive = self.dossier_archives / nom_archive
            
            fichiers_archives = []
            
            with zipfile.ZipFile(chemin_archive, 'w', zipfile.ZIP_DEFLATED) as archive:
                for fichier_log in self.dossier_logs.glob("*.log"):
                    # Vérifier la date de modification
                    date_modif = datetime.fromtimestamp(fichier_log.stat().st_mtime)
                    
                    if date_modif < date_limite:
                        # Ajouter à l'archive
                        archive.write(fichier_log, fichier_log.name)
                        fichiers_archives.append(fichier_log.name)
                        
                        # Supprimer le fichier original
                        fichier_log.unlink()
            
            if fichiers_archives:
                print(f"✅ {len(fichiers_archives)} fichiers archivés dans {nom_archive}")
                return str(chemin_archive)
            else:
                # Supprimer l'archive vide
                chemin_archive.unlink()
                print("Aucun fichier ancien à archiver")
                return None
                
        except Exception as e:
            print(f"❌ Erreur lors de l'archivage: {e}")
            return None
    
    def generer_rapport(self, fichier_log, type_log="custom"):
        """Génère un rapport détaillé en format texte"""
        try:
            analyse = self.analyser_logs(fichier_log, type_log)
            if not analyse:
                return None
            
            nom_rapport = f"rapport_{Path(fichier_log).stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            chemin_rapport = self.dossier_archives / nom_rapport
            
            with open(chemin_rapport, "w", encoding="utf-8") as f:
                f.write(f"RAPPORT D'ANALYSE - {fichier_log}\\n")
                f.write(f"Généré le: {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}\\n")
                f.write("="*60 + "\\n\\n")
                
                if type_log == "custom":
                    f.write(f"Total d'entrées: {analyse['total_entrees']}\\n\\n")
                    
                    f.write("RÉPARTITION PAR NIVEAU:\\n")
                    for niveau, count in sorted(analyse['niveaux'].items()):
                        pourcentage = (count / analyse['total_entrees']) * 100
                        f.write(f"  {niveau:8}: {count:6} ({pourcentage:5.1f}%)\\n")
                    
                    f.write("\\nACTIVITÉ PAR HEURE:\\n")
                    for heure in sorted(analyse['messages_par_heure'].keys()):
                        count = analyse['messages_par_heure'][heure]
                        f.write(f"  {heure}: {count:4} messages\\n")
                    
                    f.write("\\nMOTS LES PLUS FRÉQUENTS:\\n")
                    for mot, freq in analyse['mots_frequents']:
                        f.write(f"  {mot:15}: {freq:4}\\n")
                
                elif type_log == "apache":
                    f.write(f"Total de requêtes: {analyse['total_requetes']}\\n")
                    f.write(f"Adresses IP uniques: {analyse['ips_uniques']}\\n\\n")
                    
                    f.write("TOP 5 ADRESSES IP:\\n")
                    for ip, count in analyse['top_ips']:
                        f.write(f"  {ip:15}: {count:6} requêtes\\n")
                    
                    f.write("\\nCODES DE STATUT:\\n")
                    for status, count in sorted(analyse['status_codes'].items()):
                        pourcentage = (count / analyse['total_requetes']) * 100
                        f.write(f"  {status:3}: {count:6} ({pourcentage:5.1f}%)\\n")
                    
                    f.write("\\nTOP 10 URLs:\\n")
                    for url, count in analyse['top_urls']:
                        f.write(f"  {count:4}: {url}\\n")
            
            print(f"✅ Rapport généré: {nom_rapport}")
            return str(chemin_rapport)
            
        except Exception as e:
            print(f"❌ Erreur lors de la génération du rapport: {e}")
            return None

# Démonstration complète
def demo_journal_manager():
    """Démonstration complète du gestionnaire de journaux"""
    jm = JournalManager()
    
    # Créer des logs de test
    print("=== Création de logs de test ===")
    messages_test = [
        ("Application démarrée", "INFO"),
        ("Utilisateur Alice connecté", "INFO"),
        ("Tentative de connexion échouée pour user123", "WARNING"),
        ("Erreur de base de données: timeout", "ERROR"),
        ("Utilisateur Bob déconnecté", "INFO"),
        ("Sauvegarde automatique effectuée", "INFO"),
        ("Tentative d'accès non autorisé depuis 192.168.1.100", "WARNING"),
        ("Système surchargé: 95% CPU", "ERROR")
    ]
    
    for message, niveau in messages_test:
        jm.ecrire_log(message, niveau, "app.log")
    
    print("✅ Logs de test créés\\n")
    
    # Analyser les logs
    print("=== Analyse des logs ===")
    analyse = jm.analyser_logs("app.log", "custom")
    if analyse:
        print(f"Total d'entrées: {analyse['total_entrees']}")
        print(f"Niveaux: {analyse['niveaux']}")
        print(f"Mots fréquents: {analyse['mots_frequents'][:5]}")
    
    print()
    
    # Exporter l'analyse
    print("=== Export de l'analyse ===")
    fichier_json = jm.exporter_analyse("app.log", "json", "custom")
    fichier_csv = jm.exporter_analyse("app.log", "csv", "custom")
    
    # Générer un rapport
    print("\\n=== Génération du rapport ===")
    rapport = jm.generer_rapport("app.log", "custom")
    
    # Lister les fichiers créés
    print("\\n=== Fichiers générés ===")
    print(f"Logs: {list(jm.dossier_logs.glob('*'))}")
    print(f"Archives: {list(jm.dossier_archives.glob('*'))}")

if __name__ == "__main__":
    demo_journal_manager()''',
                    'exercice': '''## 🎯 Exercice : Système de gestion de données étudiants

**Objectif :** Créer un système complet de gestion de données d'étudiants avec support de multiples formats de fichiers

### Partie 1 : Structure des données

Créez les classes suivantes :

```python
from dataclasses import dataclass
from datetime import date
from typing import List, Dict, Optional

@dataclass
class Etudiant:
    nom: str
    prenom: str
    age: int
    email: str
    date_inscription: date
    notes: Dict[str, float]  # {matière: note}
    
    def moyenne(self) -> float:
        # Calculer la moyenne générale
        pass
    
    def mention(self) -> str:
        # Retourner la mention selon la moyenne
        pass

class GestionnaireEtudiants:
    def __init__(self):
        self.etudiants: List[Etudiant] = []
    
    def ajouter_etudiant(self, etudiant: Etudiant):
        # À implémenter
        pass
    
    def rechercher_etudiant(self, nom: str, prenom: str) -> Optional[Etudiant]:
        # À implémenter
        pass
    
    def statistiques_classe(self) -> Dict:
        # À implémenter
        pass
```

### Partie 2 : Import/Export de données

Implémentez les méthodes suivantes :

#### Import CSV
```python
def importer_csv(self, fichier: str) -> bool:
    """
    Importe les étudiants depuis un fichier CSV
    Format: nom,prenom,age,email,date_inscription,math,francais,histoire,sciences
    """
    # À implémenter avec gestion d'erreurs
    pass
```

#### Export CSV
```python
def exporter_csv(self, fichier: str) -> bool:
    """Exporte les étudiants vers un fichier CSV"""
    # À implémenter
    pass
```

#### Import/Export JSON
```python
def sauvegarder_json(self, fichier: str) -> bool:
    """Sauvegarde en format JSON avec toutes les données"""
    # À implémenter - gérer la sérialisation des dates
    pass

def charger_json(self, fichier: str) -> bool:
    """Charge depuis un fichier JSON"""
    # À implémenter - gérer la désérialisation des dates
    pass
```

#### Sauvegarde binaire
```python
def sauvegarder_pickle(self, fichier: str) -> bool:
    """Sauvegarde binaire avec pickle"""
    pass

def charger_pickle(self, fichier: str) -> bool:
    """Charge depuis un fichier pickle"""
    pass
```

### Partie 3 : Analyse et rapports

#### Génération de rapports
```python
def generer_rapport_classe(self, fichier: str = "rapport_classe.txt"):
    """
    Génère un rapport détaillé de la classe
    Inclure:
    - Nombre total d'étudiants
    - Moyenne générale de la classe
    - Répartition des mentions
    - Top 5 des meilleurs étudiants
    - Statistiques par matière
    """
    pass

def generer_bulletin_individuel(self, nom: str, prenom: str, fichier: str = None):
    """
    Génère le bulletin d'un étudiant
    Format: nom_prenom_bulletin.txt
    """
    pass
```

#### Statistiques avancées
```python
def analyser_matieres(self) -> Dict:
    """
    Analyse les performances par matière:
    - Moyenne par matière
    - Écart-type
    - Note min/max
    - Nombre d'étudiants par mention
    """
    pass

def identifier_risques_echec(self) -> List[Etudiant]:
    """Identifie les étudiants à risque (moyenne < 8)"""
    pass

def etudiants_excellents(self) -> List[Etudiant]:
    """Étudiants avec mention Très Bien (moyenne >= 16)"""
    pass
```

### Partie 4 : Sauvegarde et historique

```python
def creer_sauvegarde_quotidienne(self):
    """
    Crée une sauvegarde horodatée
    Format: backup_YYYYMMDD_HHMMSS.json
    """
    pass

def restaurer_sauvegarde(self, fichier_sauvegarde: str) -> bool:
    """Restaure depuis une sauvegarde"""
    pass

def nettoyer_anciennes_sauvegardes(self, jours_conservation: int = 30):
    """Supprime les sauvegardes de plus de X jours"""
    pass
```

### Partie 5 : Interface utilisateur

Créez un menu interactif :

```python
def menu_principal():
    """
    Menu principal avec options:
    1. Ajouter un étudiant
    2. Rechercher un étudiant
    3. Afficher tous les étudiants
    4. Importer CSV
    5. Exporter CSV
    6. Sauvegarder JSON
    7. Charger JSON
    8. Générer rapport de classe
    9. Générer bulletin individuel
    10. Statistiques par matière
    11. Créer sauvegarde
    12. Quitter
    """
    pass
```

### Données de test

Créez un fichier `etudiants.csv` avec des données de test :

```csv
nom,prenom,age,email,date_inscription,math,francais,histoire,sciences
Dupont,Alice,20,alice.dupont@email.com,2023-09-01,15.5,14.0,16.0,17.5
Martin,Bob,19,bob.martin@email.com,2023-09-01,12.0,13.5,11.0,14.0
Bernard,Charlie,21,charlie.bernard@email.com,2023-09-01,18.0,16.5,17.0,19.0
Durand,Diana,20,diana.durand@email.com,2023-09-01,8.0,9.5,7.5,10.0
Moreau,Eve,19,eve.moreau@email.com,2023-09-01,16.0,18.0,15.5,16.5
```

### Fonctionnalités bonus

1. **Validation des données** :
   - Email valide
   - Âge cohérent (16-30 ans)
   - Notes entre 0 et 20
   - Date d'inscription valide

2. **Gestion des erreurs** :
   - Fichiers corrompus
   - Données manquantes
   - Permissions de fichier
   - Espace disque insuffisant

3. **Performance** :
   - Import/export de gros fichiers
   - Recherche optimisée
   - Cache des calculs

4. **Export avancé** :
   - Export HTML avec CSS
   - Export PDF (si bibliothèque disponible)
   - Export Excel

5. **Sécurité** :
   - Chiffrement des données sensibles
   - Validation des entrées
   - Logs d'audit

### Tests à réaliser

```python
def test_import_export():
    """Test d'import/export dans différents formats"""
    pass

def test_calculs_statistiques():
    """Test des calculs de moyennes et statistiques"""
    pass

def test_gestion_erreurs():
    """Test de la gestion d'erreurs"""
    pass

def test_sauvegarde_restauration():
    """Test du système de sauvegarde"""
    pass
```

### Exemple d'utilisation attendue

```python
# Créer le gestionnaire
gestionnaire = GestionnaireEtudiants()

# Importer des données
gestionnaire.importer_csv("etudiants.csv")

# Ajouter un étudiant
nouvel_etudiant = Etudiant(
    nom="Nouveau",
    prenom="Student", 
    age=20,
    email="student@email.com",
    date_inscription=date.today(),
    notes={"math": 15.0, "francais": 14.0}
)
gestionnaire.ajouter_etudiant(nouvel_etudiant)

# Générer des rapports
gestionnaire.generer_rapport_classe()
gestionnaire.generer_bulletin_individuel("Dupont", "Alice")

# Statistiques
stats = gestionnaire.analyser_matieres()
print(f"Moyenne math: {stats['math']['moyenne']}")

# Sauvegarde
gestionnaire.creer_sauvegarde_quotidienne()
```

**Critères de réussite :**
- Import/export fonctionnel pour CSV, JSON, Pickle
- Calculs statistiques corrects
- Gestion d'erreurs robuste
- Rapports bien formatés
- Interface utilisateur intuitive
- Performance acceptable (< 1s pour 1000 étudiants)

Ce système doit être complet, robuste et facile à utiliser ! 🎓'''
                }
            )
            
            # Chapitre 6: Introduction aux bases de données - Partie 1
            Chapitre.objects.get_or_create(
                cours=cours_avance,
                slug='intro-bases-donnees-partie1',
                defaults={
                    'titre': 'Introduction aux bases de données - Partie 1',
                    'ordre': 6,
                    'contenu': '''# Introduction aux bases de données en Python - Partie 1

## 🗄️ Qu'est-ce qu'une base de données ?

Une **base de données** est un système organisé pour stocker, gérer et récupérer des informations de manière efficace et structurée.

### Types principaux de bases de données

**1. Bases de données relationnelles**
- MySQL, PostgreSQL, SQLite
- Données organisées en tables avec relations
- Langage SQL pour les requêtes

**2. Bases de données NoSQL**
- MongoDB (documents), Redis (clé-valeur)
- Flexibles, adaptées au Big Data
- Pas de schéma fixe

**3. Bases de données en mémoire**
- Redis, Memcached
- Très rapides, volatiles

## 📊 SQLite - Base de données intégrée

SQLite est parfait pour débuter : léger, sans configuration, intégré à Python !

### Premier exemple
```python
import sqlite3

# Connexion (fichier créé automatiquement)
connexion = sqlite3.connect('ma_base.db')
curseur = connexion.cursor()

# Créer une table
curseur.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    )
""")

# Insérer des données
curseur.execute(
    "INSERT INTO utilisateurs (nom, email, age) VALUES (?, ?, ?)",
    ("Alice Dupont", "alice@email.com", 25)
)

# Sauvegarder et fermer
connexion.commit()
connexion.close()

print("✅ Base de données créée !")
```

### Opérations de base (CRUD)
```python
import sqlite3

def creer_table():
    """Crée la table des utilisateurs"""
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER CHECK(age > 0)
            )
        """)
        conn.commit()

def ajouter_utilisateur(nom, email, age):
    """Ajoute un nouvel utilisateur (CREATE)"""
    try:
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (nom, email, age) VALUES (?, ?, ?)",
                (nom, email, age)
            )
            conn.commit()
            print(f"✅ Utilisateur {nom} ajouté !")
            return cursor.lastrowid
    except sqlite3.IntegrityError:
        print("❌ Email déjà utilisé")
        return None

def lire_utilisateurs():
    """Lit tous les utilisateurs (READ)"""
    with sqlite3.connect('users.db') as conn:
        conn.row_factory = sqlite3.Row  # Pour des colonnes nommées
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        
        users = []
        for row in cursor.fetchall():
            users.append({
                'id': row['id'],
                'nom': row['nom'],
                'email': row['email'],
                'age': row['age']
            })
        return users

def modifier_utilisateur(user_id, nouveau_nom=None, nouvel_age=None):
    """Modifie un utilisateur (UPDATE)"""
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        
        if nouveau_nom:
            cursor.execute(
                "UPDATE users SET nom = ? WHERE id = ?",
                (nouveau_nom, user_id)
            )
        
        if nouvel_age:
            cursor.execute(
                "UPDATE users SET age = ? WHERE id = ?",
                (nouvel_age, user_id)
            )
        
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Utilisateur {user_id} modifié")
            return True
        else:
            print("❌ Utilisateur non trouvé")
            return False

def supprimer_utilisateur(user_id):
    """Supprime un utilisateur (DELETE)"""
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Utilisateur {user_id} supprimé")
            return True
        else:
            print("❌ Utilisateur non trouvé")
            return False
```

### Démonstration pratique
```python
def demo_sqlite():
    """Démonstration complète de SQLite"""
    
    # Créer la table
    creer_table()
    
    # Ajouter des utilisateurs
    print("=== AJOUT D'UTILISATEURS ===")
    id1 = ajouter_utilisateur("Alice Martin", "alice@test.com", 28)
    id2 = ajouter_utilisateur("Bob Durand", "bob@test.com", 35)
    id3 = ajouter_utilisateur("Charlie Roy", "charlie@test.com", 42)
    
    # Lire tous les utilisateurs
    print("\\n=== LISTE DES UTILISATEURS ===")
    utilisateurs = lire_utilisateurs()
    for user in utilisateurs:
        print(f"- {user['nom']} ({user['age']} ans) - {user['email']}")
    
    # Modifier un utilisateur
    print("\\n=== MODIFICATION ===")
    if id1:
        modifier_utilisateur(id1, nouveau_nom="Alice Martin-Dupont")
    
    # Vérifier la modification
    utilisateurs = lire_utilisateurs()
    for user in utilisateurs:
        if user['id'] == id1:
            print(f"Nom modifié : {user['nom']}")
    
    # Supprimer un utilisateur
    print("\\n=== SUPPRESSION ===")
    if id3:
        supprimer_utilisateur(id3)
    
    # Afficher le résultat final
    print("\\n=== RÉSULTAT FINAL ===")
    utilisateurs = lire_utilisateurs()
    for user in utilisateurs:
        print(f"- {user['nom']} ({user['age']} ans)")
    
    print(f"\\nNombre total d'utilisateurs : {len(utilisateurs)}")

if __name__ == "__main__":
    demo_sqlite()
```

## 🛠️ Bonnes pratiques avec SQLite

### 1. Utilisation du context manager
```python
# Recommandé : fermeture automatique
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    # Vos opérations ici
    # Commit automatique à la fin
```

### 2. Paramètres liés (éviter l'injection SQL)
```python
# ❌ Dangereux
query = f"SELECT * FROM users WHERE name = '{name}'"

# ✅ Sécurisé
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

### 3. Gestion des erreurs
```python
try:
    cursor.execute("INSERT INTO users ...")
    conn.commit()
except sqlite3.IntegrityError as e:
    print(f"Erreur de contrainte : {e}")
except sqlite3.Error as e:
    print(f"Erreur SQLite : {e}")
```

### 4. Row factory pour des résultats lisibles
```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(f"Nom: {row['nom']}, Email: {row['email']}")
```

La **Partie 2** couvrira les relations entre tables et les requêtes avancées ! 🚀''',
                    'code_exemple': '''# Exemple complet : Carnet d'adresses avec SQLite

import sqlite3
import json
from datetime import datetime, date
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict

@dataclass
class Contact:
    nom: str
    prenom: str
    email: str
    telephone: str = None
    adresse: str = None
    ville: str = None
    date_ajout: date = None
    id: Optional[int] = None
    
    def __post_init__(self):
        if self.date_ajout is None:
            self.date_ajout = date.today()

class CarnetAdresses:
    """Gestionnaire de carnet d'adresses avec SQLite"""
    
    def __init__(self, db_name="contacts.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialise la base de données"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Table principale des contacts
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL,
                    email TEXT UNIQUE,
                    telephone TEXT,
                    adresse TEXT,
                    ville TEXT,
                    date_ajout DATE NOT NULL,
                    date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Index pour optimiser les recherches
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_nom ON contacts(nom)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON contacts(email)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_ville ON contacts(ville)")
            
            conn.commit()
            print("✅ Base de données initialisée")
    
    def ajouter_contact(self, contact: Contact) -> Optional[int]:
        """Ajoute un nouveau contact"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO contacts 
                    (nom, prenom, email, telephone, adresse, ville, date_ajout)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    contact.nom, contact.prenom, contact.email, 
                    contact.telephone, contact.adresse, contact.ville,
                    contact.date_ajout
                ))
                
                contact_id = cursor.lastrowid
                conn.commit()
                
                print(f"✅ Contact {contact.prenom} {contact.nom} ajouté (ID: {contact_id})")
                return contact_id
                
        except sqlite3.IntegrityError:
            print(f"❌ Email {contact.email} déjà utilisé")
            return None
        except sqlite3.Error as e:
            print(f"❌ Erreur lors de l'ajout: {e}")
            return None
    
    def obtenir_contact(self, contact_id: int) -> Optional[Contact]:
        """Récupère un contact par son ID"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
            row = cursor.fetchone()
            
            if row:
                return Contact(
                    id=row['id'],
                    nom=row['nom'],
                    prenom=row['prenom'],
                    email=row['email'],
                    telephone=row['telephone'],
                    adresse=row['adresse'],
                    ville=row['ville'],
                    date_ajout=datetime.fromisoformat(row['date_ajout']).date()
                )
        return None
    
    def lister_contacts(self, limite: int = None, ordre: str = 'nom') -> List[Contact]:
        """Liste tous les contacts"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            query = f"SELECT * FROM contacts ORDER BY {ordre}, prenom"
            if limite:
                query += f" LIMIT {limite}"
            
            cursor.execute(query)
            
            contacts = []
            for row in cursor.fetchall():
                contacts.append(Contact(
                    id=row['id'],
                    nom=row['nom'],
                    prenom=row['prenom'],
                    email=row['email'],
                    telephone=row['telephone'],
                    adresse=row['adresse'],
                    ville=row['ville'],
                    date_ajout=datetime.fromisoformat(row['date_ajout']).date()
                ))
            
            return contacts
    
    def rechercher_contacts(self, terme: str) -> List[Contact]:
        """Recherche des contacts par nom, prénom, email ou ville"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            pattern = f"%{terme}%"
            cursor.execute("""
                SELECT * FROM contacts 
                WHERE nom LIKE ? OR prenom LIKE ? OR email LIKE ? OR ville LIKE ?
                ORDER BY nom, prenom
            """, (pattern, pattern, pattern, pattern))
            
            contacts = []
            for row in cursor.fetchall():
                contacts.append(Contact(
                    id=row['id'],
                    nom=row['nom'],
                    prenom=row['prenom'],
                    email=row['email'],
                    telephone=row['telephone'],
                    adresse=row['adresse'],
                    ville=row['ville'],
                    date_ajout=datetime.fromisoformat(row['date_ajout']).date()
                ))
            
            return contacts
    
    def contacts_par_ville(self, ville: str) -> List[Contact]:
        """Récupère tous les contacts d'une ville"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute(
                "SELECT * FROM contacts WHERE ville = ? ORDER BY nom, prenom",
                (ville,)
            )
            
            return [Contact(
                id=row['id'],
                nom=row['nom'],
                prenom=row['prenom'],
                email=row['email'],
                telephone=row['telephone'],
                adresse=row['adresse'],
                ville=row['ville'],
                date_ajout=datetime.fromisoformat(row['date_ajout']).date()
            ) for row in cursor.fetchall()]
    
    def modifier_contact(self, contact_id: int, **modifications) -> bool:
        """Modifie les informations d'un contact"""
        if not modifications:
            return False
            
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Construire la requête dynamiquement
                champs_valides = {'nom', 'prenom', 'email', 'telephone', 'adresse', 'ville'}
                champs = []
                valeurs = []
                
                for champ, valeur in modifications.items():
                    if champ in champs_valides:
                        champs.append(f"{champ} = ?")
                        valeurs.append(valeur)
                
                if champs:
                    # Ajouter la date de modification
                    champs.append("date_modification = ?")
                    valeurs.append(datetime.now())
                    
                    query = f"UPDATE contacts SET {', '.join(champs)} WHERE id = ?"
                    valeurs.append(contact_id)
                    
                    cursor.execute(query, valeurs)
                    
                    if cursor.rowcount > 0:
                        conn.commit()
                        print(f"✅ Contact {contact_id} modifié")
                        return True
                    else:
                        print("❌ Contact non trouvé")
                        return False
            
            return False
            
        except sqlite3.IntegrityError:
            print("❌ Email déjà utilisé par un autre contact")
            return False
        except sqlite3.Error as e:
            print(f"❌ Erreur lors de la modification: {e}")
            return False
    
    def supprimer_contact(self, contact_id: int) -> bool:
        """Supprime un contact"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
                
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"✅ Contact {contact_id} supprimé")
                    return True
                else:
                    print("❌ Contact non trouvé")
                    return False
                    
        except sqlite3.Error as e:
            print(f"❌ Erreur lors de la suppression: {e}")
            return False
    
    def statistiques(self) -> Dict:
        """Calcule des statistiques sur le carnet"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Nombre total de contacts
            cursor.execute("SELECT COUNT(*) FROM contacts")
            total_contacts = cursor.fetchone()[0]
            
            # Répartition par ville
            cursor.execute("""
                SELECT ville, COUNT(*) as nombre 
                FROM contacts 
                WHERE ville IS NOT NULL 
                GROUP BY ville 
                ORDER BY nombre DESC
            """)
            par_ville = cursor.fetchall()
            
            # Contacts récents (7 derniers jours)
            cursor.execute("""
                SELECT COUNT(*) 
                FROM contacts 
                WHERE date_ajout >= date('now', '-7 days')
            """)
            recents = cursor.fetchone()[0]
            
            # Contacts avec email
            cursor.execute("SELECT COUNT(*) FROM contacts WHERE email IS NOT NULL")
            avec_email = cursor.fetchone()[0]
            
            # Contacts avec téléphone
            cursor.execute("SELECT COUNT(*) FROM contacts WHERE telephone IS NOT NULL")
            avec_telephone = cursor.fetchone()[0]
            
            return {
                'total_contacts': total_contacts,
                'repartition_villes': par_ville,
                'contacts_recents': recents,
                'avec_email': avec_email,
                'avec_telephone': avec_telephone,
                'pourcentage_email': round((avec_email / total_contacts) * 100, 1) if total_contacts > 0 else 0,
                'pourcentage_telephone': round((avec_telephone / total_contacts) * 100, 1) if total_contacts > 0 else 0
            }
    
    def exporter_json(self, fichier: str = None) -> str:
        """Exporte tous les contacts en JSON"""
        if not fichier:
            fichier = f"contacts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        contacts = self.lister_contacts()
        data = {
            'export_date': datetime.now().isoformat(),
            'total_contacts': len(contacts),
            'contacts': [asdict(contact) for contact in contacts]
        }
        
        # Convertir les dates en string pour JSON
        for contact in data['contacts']:
            if contact['date_ajout']:
                contact['date_ajout'] = contact['date_ajout'].isoformat()
        
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Contacts exportés vers {fichier}")
        return fichier
    
    def importer_json(self, fichier: str) -> int:
        """Importe des contacts depuis un fichier JSON"""
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            contacts_ajoutes = 0
            
            for contact_data in data.get('contacts', []):
                # Convertir la date string en date
                if 'date_ajout' in contact_data and contact_data['date_ajout']:
                    contact_data['date_ajout'] = datetime.fromisoformat(contact_data['date_ajout']).date()
                
                # Retirer l'ID pour éviter les conflits
                contact_data.pop('id', None)
                
                contact = Contact(**contact_data)
                if self.ajouter_contact(contact):
                    contacts_ajoutes += 1
            
            print(f"✅ {contacts_ajoutes} contacts importés sur {len(data.get('contacts', []))}")
            return contacts_ajoutes
            
        except FileNotFoundError:
            print(f"❌ Fichier {fichier} non trouvé")
            return 0
        except json.JSONDecodeError:
            print("❌ Fichier JSON invalide")
            return 0
        except Exception as e:
            print(f"❌ Erreur lors de l'import: {e}")
            return 0

def menu_carnet():
    """Menu interactif pour le carnet d'adresses"""
    carnet = CarnetAdresses()
    
    while True:
        print("\\n" + "="*50)
        print("           CARNET D'ADRESSES")
        print("="*50)
        print("1. Ajouter un contact")
        print("2. Rechercher des contacts")
        print("3. Lister tous les contacts")
        print("4. Contacts par ville")
        print("5. Modifier un contact")
        print("6. Supprimer un contact")
        print("7. Statistiques")
        print("8. Exporter en JSON")
        print("9. Importer depuis JSON")
        print("0. Quitter")
        
        choix = input("\\nVotre choix: ").strip()
        
        if choix == '1':
            # Ajouter un contact
            print("\\n--- Ajouter un contact ---")
            nom = input("Nom: ").strip()
            prenom = input("Prénom: ").strip()
            email = input("Email: ").strip() or None
            telephone = input("Téléphone: ").strip() or None
            adresse = input("Adresse: ").strip() or None
            ville = input("Ville: ").strip() or None
            
            if nom and prenom:
                contact = Contact(nom, prenom, email, telephone, adresse, ville)
                carnet.ajouter_contact(contact)
            else:
                print("❌ Nom et prénom obligatoires")
        
        elif choix == '2':
            # Rechercher
            terme = input("\\nTerme de recherche: ").strip()
            if terme:
                resultats = carnet.rechercher_contacts(terme)
                print(f"\\n{len(resultats)} résultat(s) trouvé(s):")
                for contact in resultats:
                    print(f"  {contact.prenom} {contact.nom} - {contact.email or 'Pas d\\'email'} - {contact.ville or 'Pas de ville'}")
        
        elif choix == '3':
            # Lister tous
            contacts = carnet.lister_contacts()
            print(f"\\n{len(contacts)} contact(s) total:")
            for contact in contacts:
                print(f"  {contact.prenom} {contact.nom} ({contact.ville or 'Ville inconnue'})")
        
        elif choix == '7':
            # Statistiques
            stats = carnet.statistiques()
            print("\\n--- Statistiques ---")
            print(f"Total de contacts: {stats['total_contacts']}")
            print(f"Contacts récents (7j): {stats['contacts_recents']}")
            print(f"Avec email: {stats['avec_email']} ({stats['pourcentage_email']}%)")
            print(f"Avec téléphone: {stats['avec_telephone']} ({stats['pourcentage_telephone']}%)")
            
            print("\\nRépartition par ville:")
            for ville, nombre in stats['repartition_villes'][:5]:
                print(f"  {ville}: {nombre} contact(s)")
        
        elif choix == '8':
            # Export JSON
            fichier = carnet.exporter_json()
        
        elif choix == '0':
            print("À bientôt ! 👋")
            break
        
        else:
            print("❌ Choix invalide")

def demo_carnet():
    """Démonstration du carnet d'adresses"""
    carnet = CarnetAdresses()
    
    # Ajouter quelques contacts d'exemple
    contacts_test = [
        Contact("Dupont", "Jean", "jean.dupont@email.com", "0123456789", "1 rue de la Paix", "Paris"),
        Contact("Martin", "Sophie", "sophie.martin@email.com", "0987654321", "5 avenue Victor Hugo", "Lyon"),
        Contact("Durand", "Pierre", "pierre.durand@email.com", None, "10 boulevard Saint-Michel", "Paris"),
        Contact("Moreau", "Marie", "marie.moreau@email.com", "0147258369", None, "Marseille"),
        Contact("Garcia", "Carlos", None, "0654321987", "2 place du Marché", "Toulouse")
    ]
    
    print("=== Ajout de contacts de test ===")
    for contact in contacts_test:
        carnet.ajouter_contact(contact)
    
    print("\\n=== Recherche 'Dupont' ===")
    resultats = carnet.rechercher_contacts("Dupont")
    for contact in resultats:
        print(f"Trouvé: {contact.prenom} {contact.nom}")
    
    print("\\n=== Contacts de Paris ===")
    parisiens = carnet.contacts_par_ville("Paris")
    for contact in parisiens:
        print(f"Parisien: {contact.prenom} {contact.nom}")
    
    print("\\n=== Statistiques ===")
    stats = carnet.statistiques()
    print(f"Total: {stats['total_contacts']} contacts")
    print(f"Avec email: {stats['pourcentage_email']}%")
    
    print("\\n=== Export JSON ===")
    fichier_export = carnet.exporter_json()

if __name__ == "__main__":
    # Choisir entre démo et menu interactif
    choix = input("Démo automatique (d) ou menu interactif (m) ? ").lower()
    
    if choix == 'd':
        demo_carnet()
    else:
        menu_carnet()''',
                    'exercice': '''## 🎯 Exercice : Gestionnaire de notes d'étudiants (SQLite)

**Objectif :** Créer un système de gestion des notes avec SQLite

### Partie 1 : Structure de base

Créez un système avec les tables suivantes :

#### Table des étudiants
```sql
CREATE TABLE etudiants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    date_naissance DATE,
    classe TEXT NOT NULL,
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Table des matières
```sql
CREATE TABLE matieres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL UNIQUE,
    coefficient REAL DEFAULT 1.0,
    couleur TEXT DEFAULT '#3498db'
);
```

#### Table des notes
```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    etudiant_id INTEGER NOT NULL,
    matiere_id INTEGER NOT NULL,
    note REAL CHECK(note >= 0 AND note <= 20),
    type_evaluation TEXT NOT NULL,
    date_evaluation DATE NOT NULL,
    commentaire TEXT,
    FOREIGN KEY (etudiant_id) REFERENCES etudiants (id),
    FOREIGN KEY (matiere_id) REFERENCES matieres (id)
);
```

### Partie 2 : Classes Python

```python
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Dict
import sqlite3

@dataclass
class Etudiant:
    nom: str
    prenom: str
    email: str
    classe: str
    date_naissance: date = None
    id: Optional[int] = None

@dataclass
class Matiere:
    nom: str
    coefficient: float = 1.0
    couleur: str = '#3498db'
    id: Optional[int] = None

@dataclass
class Note:
    etudiant_id: int
    matiere_id: int
    note: float
    type_evaluation: str
    date_evaluation: date
    commentaire: str = None
    id: Optional[int] = None

class GestionnaireNotes:
    def __init__(self, db_name="notes_etudiants.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialise la base de données"""
        # À implémenter
        pass
    
    # === GESTION DES ÉTUDIANTS ===
    
    def ajouter_etudiant(self, etudiant: Etudiant) -> Optional[int]:
        """Ajoute un nouvel étudiant"""
        # À implémenter avec validation email unique
        pass
    
    def lister_etudiants(self, classe: str = None) -> List[Etudiant]:
        """Liste les étudiants, optionnellement par classe"""
        pass
    
    def rechercher_etudiants(self, terme: str) -> List[Etudiant]:
        """Recherche par nom, prénom ou email"""
        pass
    
    # === GESTION DES MATIÈRES ===
    
    def ajouter_matiere(self, matiere: Matiere) -> Optional[int]:
        """Ajoute une nouvelle matière"""
        pass
    
    def lister_matieres(self) -> List[Matiere]:
        """Liste toutes les matières"""
        pass
    
    # === GESTION DES NOTES ===
    
    def ajouter_note(self, note: Note) -> Optional[int]:
        """Ajoute une note"""
        # Validation : note entre 0 et 20
        pass
    
    def notes_etudiant(self, etudiant_id: int, matiere_id: int = None) -> List[Note]:
        """Récupère les notes d'un étudiant"""
        pass
    
    def notes_matiere(self, matiere_id: int, classe: str = None) -> List[Dict]:
        """Notes d'une matière, optionnellement par classe"""
        pass
    
    # === CALCULS ET STATISTIQUES ===
    
    def moyenne_etudiant(self, etudiant_id: int, matiere_id: int = None) -> float:
        """Calcule la moyenne d'un étudiant"""
        # Si matiere_id est None, moyenne générale avec coefficients
        pass
    
    def moyenne_classe(self, classe: str, matiere_id: int = None) -> float:
        """Calcule la moyenne d'une classe"""
        pass
    
    def rang_etudiant(self, etudiant_id: int, classe: str) -> int:
        """Détermine le rang d'un étudiant dans sa classe"""
        pass
    
    def bulletin_etudiant(self, etudiant_id: int) -> Dict:
        """Génère le bulletin complet d'un étudiant"""
        # Inclure :
        # - Moyenne par matière
        # - Moyenne générale
        # - Rang dans la classe
        # - Nombre de notes par matière
        pass
    
    def statistiques_matiere(self, matiere_id: int) -> Dict:
        """Statistiques complètes d'une matière"""
        # Inclure :
        # - Moyenne générale
        # - Note min/max
        # - Nombre d'étudiants
        # - Répartition des notes
        pass
```

### Partie 3 : Fonctionnalités avancées

#### A. Système de mentions
```python
def obtenir_mention(self, moyenne: float) -> str:
    """Détermine la mention selon la moyenne"""
    if moyenne >= 16:
        return "Très Bien"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez Bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Insuffisant"

def repartition_mentions(self, classe: str) -> Dict:
    """Répartition des mentions dans une classe"""
    pass
```

#### B. Analyses temporelles
```python
def evolution_notes_etudiant(self, etudiant_id: int, matiere_id: int) -> List[Dict]:
    """Évolution des notes dans le temps"""
    pass

def evolution_moyenne_classe(self, classe: str, matiere_id: int) -> List[Dict]:
    """Évolution de la moyenne de classe"""
    pass
```

#### C. Import/Export
```python
def importer_notes_csv(self, fichier: str) -> int:
    """Importe des notes depuis un CSV"""
    # Format: nom,prenom,matiere,note,type_evaluation,date
    pass

def exporter_bulletin_pdf(self, etudiant_id: int) -> str:
    """Exporte un bulletin en PDF (bonus)"""
    pass

def exporter_statistiques_classe(self, classe: str, format_sortie: str = "json") -> str:
    """Exporte les statistiques d'une classe"""
    pass
```

### Partie 4 : Interface utilisateur

Créez un menu avec :

1. **Gestion des étudiants**
   - Ajouter/modifier un étudiant
   - Lister par classe
   - Rechercher

2. **Gestion des matières**
   - Ajouter une matière
   - Modifier coefficients
   - Lister toutes

3. **Saisie des notes**
   - Ajouter une note
   - Notes par étudiant
   - Notes par matière

4. **Bulletins et moyennes**
   - Bulletin individuel
   - Moyennes de classe
   - Classements

5. **Statistiques**
   - Par matière
   - Par classe
   - Évolutions temporelles

### Partie 5 : Données de test

Créez des données réalistes :
```python
def creer_donnees_test():
    """Crée des données de test"""
    # 3 classes : 6èmeA, 5èmeB, 4èmeC
    # 5-8 étudiants par classe
    # 5 matières : Math, Français, Anglais, Histoire, Sciences
    # 3-5 notes par étudiant par matière
    pass
```

### Partie 6 : Tests

```python
import unittest

class TestGestionnaireNotes(unittest.TestCase):
    def setUp(self):
        self.gestionnaire = GestionnaireNotes("test_notes.db")
    
    def test_calcul_moyenne(self):
        """Test du calcul de moyenne"""
        # Tester avec différents coefficients
        pass
    
    def test_rang_etudiant(self):
        """Test du calcul de rang"""
        pass
    
    def test_contraintes(self):
        """Test des contraintes (note 0-20, etc.)"""
        pass
```

### Fonctionnalités bonus

1. **Graphiques** de progression avec matplotlib
2. **Système d'alertes** pour notes faibles
3. **Prédictions** de moyenne finale
4. **Comparaisons** entre classes/années
5. **Notifications** par email aux parents
6. **Interface web** avec Flask
7. **API REST** pour mobile

### Données de test CSV

Créez `notes_test.csv` :
```csv
nom,prenom,email,classe,matiere,note,type_evaluation,date_evaluation
Dupont,Alice,alice.dupont@school.com,6èmeA,Mathématiques,15.5,Contrôle,2024-01-15
Dupont,Alice,alice.dupont@school.com,6èmeA,Français,14.0,Rédaction,2024-01-20
Martin,Bob,bob.martin@school.com,6èmeA,Mathématiques,12.0,Contrôle,2024-01-15
Martin,Bob,bob.martin@school.com,6èmeA,Français,16.5,Rédaction,2024-01-20
```

### Critères de réussite

- ✅ Structure de base fonctionnelle
- ✅ Calculs de moyennes corrects (avec coefficients)
- ✅ Système de rang et classements
- ✅ Bulletins complets et lisibles
- ✅ Import/export de données
- ✅ Interface utilisateur ergonomique
- ✅ Statistiques pertinentes
- ✅ Performance correcte (500+ étudiants)

**Challenge :** Le système doit gérer un collège entier ! 🎓'''
                }
            )
            
            # Chapitre 6: Relations et JOINs SQLite - Partie 2A
            Chapitre.objects.get_or_create(
                cours=cours_avance,
                slug='relations-joins-sqlite-partie2a',
                defaults={
                    'titre': 'Relations et JOINs SQLite - Partie 2A',
                    'ordre': 7,
                    'contenu': '''# Relations et JOINs SQLite - Partie 2A

## 🔗 Relations entre tables

### Pourquoi utiliser des relations ?
Au lieu de dupliquer les données, nous créons des **relations** entre les tables pour :
- ✅ **Éviter la redondance** des données
- ✅ **Maintenir la cohérence** 
- ✅ **Optimiser l'espace** de stockage
- ✅ **Faciliter les mises à jour**

### Types de relations

**1. Un-à-Un (1:1)**
```
Utilisateur ↔ Profil
Un utilisateur a un seul profil
```

**2. Un-à-Plusieurs (1:N)**
```
Client → Commandes
Un client peut avoir plusieurs commandes
```

**3. Plusieurs-à-Plusieurs (N:N)**
```
Étudiants ↔ Cours
Un étudiant suit plusieurs cours
Un cours a plusieurs étudiants
```

## 🗝️ Clés étrangères (Foreign Keys)

### Syntaxe de base
```sql
CREATE TABLE commandes (
    id INTEGER PRIMARY KEY,
    client_id INTEGER NOT NULL,
    date_commande DATE,
    total REAL,
    FOREIGN KEY (client_id) REFERENCES clients (id)
);
```

### Exemple complet avec contraintes
```python
import sqlite3
from datetime import date, datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Client:
    nom: str
    email: str
    telephone: str = None
    adresse: str = None
    id: Optional[int] = None

@dataclass
class Produit:
    nom: str
    prix: float
    stock: int = 0
    description: str = None
    id: Optional[int] = None

@dataclass
class Commande:
    client_id: int
    date_commande: date = None
    statut: str = "en_cours"
    id: Optional[int] = None
    
    def __post_init__(self):
        if self.date_commande is None:
            self.date_commande = date.today()

class BoutiqueBD:
    """Système de boutique avec relations"""
    
    def __init__(self, db_name="boutique.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Crée les tables avec relations"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Table des clients
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    telephone TEXT,
                    adresse TEXT,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Table des produits
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prix REAL NOT NULL CHECK(prix > 0),
                    stock INTEGER DEFAULT 0 CHECK(stock >= 0),
                    description TEXT,
                    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Table des commandes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS commandes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    date_commande DATE NOT NULL,
                    statut TEXT DEFAULT 'en_cours',
                    total REAL DEFAULT 0,
                    FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE
                )
            """)
            
            # Table de liaison commandes-produits (N:N)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS commande_produits (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    commande_id INTEGER NOT NULL,
                    produit_id INTEGER NOT NULL,
                    quantite INTEGER NOT NULL CHECK(quantite > 0),
                    prix_unitaire REAL NOT NULL,
                    FOREIGN KEY (commande_id) REFERENCES commandes (id) ON DELETE CASCADE,
                    FOREIGN KEY (produit_id) REFERENCES produits (id) ON DELETE CASCADE,
                    UNIQUE(commande_id, produit_id)
                )
            """)
            
            # Index pour optimiser les requêtes
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_commandes_client ON commandes(client_id)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_commande_produits_commande ON commande_produits(commande_id)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_commande_produits_produit ON commande_produits(produit_id)")
            
            conn.commit()
            print("✅ Base de données initialisée avec relations")
    
    def ajouter_client(self, client: Client) -> Optional[int]:
        """Ajoute un nouveau client"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO clients (nom, email, telephone, adresse)
                    VALUES (?, ?, ?, ?)
                """, (client.nom, client.email, client.telephone, client.adresse))
                
                client_id = cursor.lastrowid
                conn.commit()
                print(f"✅ Client {client.nom} ajouté (ID: {client_id})")
                return client_id
        except sqlite3.IntegrityError:
            print(f"❌ Email {client.email} déjà utilisé")
            return None
    
    def ajouter_produit(self, produit: Produit) -> Optional[int]:
        """Ajoute un nouveau produit"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO produits (nom, prix, stock, description)
                    VALUES (?, ?, ?, ?)
                """, (produit.nom, produit.prix, produit.stock, produit.description))
                
                produit_id = cursor.lastrowid
                conn.commit()
                print(f"✅ Produit {produit.nom} ajouté (ID: {produit_id})")
                return produit_id
        except Exception as e:
            print(f"❌ Erreur ajout produit: {e}")
            return None
    
    def creer_commande(self, client_id: int) -> Optional[int]:
        """Crée une nouvelle commande pour un client"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Vérifier que le client existe
                cursor.execute("SELECT id FROM clients WHERE id = ?", (client_id,))
                if not cursor.fetchone():
                    print(f"❌ Client {client_id} non trouvé")
                    return None
                
                # Créer la commande
                cursor.execute("""
                    INSERT INTO commandes (client_id, date_commande)
                    VALUES (?, ?)
                """, (client_id, date.today()))
                
                commande_id = cursor.lastrowid
                conn.commit()
                print(f"✅ Commande {commande_id} créée pour client {client_id}")
                return commande_id
        except Exception as e:
            print(f"❌ Erreur création commande: {e}")
            return None
    
    def ajouter_produit_commande(self, commande_id: int, produit_id: int, quantite: int) -> bool:
        """Ajoute un produit à une commande"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Récupérer le prix du produit et vérifier le stock
                cursor.execute("SELECT prix, stock FROM produits WHERE id = ?", (produit_id,))
                result = cursor.fetchone()
                
                if not result:
                    print(f"❌ Produit {produit_id} non trouvé")
                    return False
                
                prix, stock = result
                if stock < quantite:
                    print(f"❌ Stock insuffisant (disponible: {stock}, demandé: {quantite})")
                    return False
                
                # Ajouter à la commande
                cursor.execute("""
                    INSERT INTO commande_produits (commande_id, produit_id, quantite, prix_unitaire)
                    VALUES (?, ?, ?, ?)
                """, (commande_id, produit_id, quantite, prix))
                
                # Décrémenter le stock
                cursor.execute("""
                    UPDATE produits SET stock = stock - ? WHERE id = ?
                """, (quantite, produit_id))
                
                # Recalculer le total de la commande
                self._recalculer_total_commande(cursor, commande_id)
                
                conn.commit()
                print(f"✅ {quantite}x produit {produit_id} ajouté à commande {commande_id}")
                return True
                
        except sqlite3.IntegrityError:
            print("❌ Produit déjà dans cette commande")
            return False
        except Exception as e:
            print(f"❌ Erreur ajout produit: {e}")
            return False
    
    def _recalculer_total_commande(self, cursor, commande_id: int):
        """Recalcule le total d'une commande"""
        cursor.execute("""
            UPDATE commandes 
            SET total = (
                SELECT COALESCE(SUM(quantite * prix_unitaire), 0)
                FROM commande_produits 
                WHERE commande_id = ?
            )
            WHERE id = ?
        """, (commande_id, commande_id))
```

## 🔄 Requêtes JOIN

### Types de JOINs

**INNER JOIN** : Seulement les enregistrements qui ont une correspondance dans les deux tables
```sql
SELECT clients.nom, commandes.date_commande, commandes.total
FROM clients
INNER JOIN commandes ON clients.id = commandes.client_id;
```

**LEFT JOIN** : Tous les enregistrements de la table de gauche + correspondances
```sql
SELECT clients.nom, COUNT(commandes.id) as nb_commandes
FROM clients
LEFT JOIN commandes ON clients.id = commandes.client_id
GROUP BY clients.id;
```

### Implémentation Python
```python
def commandes_client(self, client_id: int) -> List[dict]:
    """Récupère toutes les commandes d'un client avec détails"""
    with sqlite3.connect(self.db_name) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                c.id,
                c.date_commande,
                c.statut,
                c.total,
                cl.nom as nom_client
            FROM commandes c
            INNER JOIN clients cl ON c.client_id = cl.id
            WHERE c.client_id = ?
            ORDER BY c.date_commande DESC
        """, (client_id,))
        
        return [dict(row) for row in cursor.fetchall()]

def produits_commande(self, commande_id: int) -> List[dict]:
    """Détaille les produits d'une commande"""
    with sqlite3.connect(self.db_name) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                p.nom,
                p.description,
                cp.quantite,
                cp.prix_unitaire,
                (cp.quantite * cp.prix_unitaire) as sous_total
            FROM commande_produits cp
            INNER JOIN produits p ON cp.produit_id = p.id
            WHERE cp.commande_id = ?
            ORDER BY p.nom
        """, (commande_id,))
        
        return [dict(row) for row in cursor.fetchall()]

def rapport_ventes(self) -> dict:
    """Rapport global des ventes"""
    with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        
        # Total des ventes
        cursor.execute("SELECT COALESCE(SUM(total), 0) FROM commandes")
        total_ventes = cursor.fetchone()[0]
        
        # Nombre de commandes
        cursor.execute("SELECT COUNT(*) FROM commandes")
        nb_commandes = cursor.fetchone()[0]
        
        # Produit le plus vendu
        cursor.execute("""
            SELECT 
                p.nom,
                SUM(cp.quantite) as total_vendu
            FROM commande_produits cp
            INNER JOIN produits p ON cp.produit_id = p.id
            GROUP BY cp.produit_id
            ORDER BY total_vendu DESC
            LIMIT 1
        """)
        produit_top = cursor.fetchone()
        
        # Client le plus actif
        cursor.execute("""
            SELECT 
                cl.nom,
                COUNT(c.id) as nb_commandes,
                COALESCE(SUM(c.total), 0) as total_achats
            FROM clients cl
            LEFT JOIN commandes c ON cl.id = c.client_id
            GROUP BY cl.id
            ORDER BY total_achats DESC
            LIMIT 1
        """)
        client_top = cursor.fetchone()
        
        return {
            'total_ventes': total_ventes,
            'nombre_commandes': nb_commandes,
            'panier_moyen': round(total_ventes / nb_commandes, 2) if nb_commandes > 0 else 0,
            'produit_top': produit_top,
            'client_top': client_top
        }

def clients_sans_commande(self) -> List[dict]:
    """Trouve les clients qui n'ont jamais commandé"""
    with sqlite3.connect(self.db_name) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT cl.id, cl.nom, cl.email
            FROM clients cl
            LEFT JOIN commandes c ON cl.id = c.client_id
            WHERE c.id IS NULL
            ORDER BY cl.nom
        """)
        
        return [dict(row) for row in cursor.fetchall()]
```

## 📊 Agrégations avancées

### GROUP BY et fonctions d'agrégation
```python
def statistiques_par_client(self) -> List[dict]:
    """Statistiques détaillées par client"""
    with sqlite3.connect(self.db_name) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                cl.nom,
                cl.email,
                COUNT(c.id) as nb_commandes,
                COALESCE(SUM(c.total), 0) as total_achats,
                COALESCE(AVG(c.total), 0) as panier_moyen,
                MIN(c.date_commande) as premiere_commande,
                MAX(c.date_commande) as derniere_commande
            FROM clients cl
            LEFT JOIN commandes c ON cl.id = c.client_id
            GROUP BY cl.id, cl.nom, cl.email
            ORDER BY total_achats DESC
        """)
        
        return [dict(row) for row in cursor.fetchall()]

def analyse_produits(self) -> List[dict]:
    """Analyse des performances des produits"""
    with sqlite3.connect(self.db_name) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                p.nom,
                p.prix,
                p.stock,
                COALESCE(SUM(cp.quantite), 0) as total_vendu,
                COALESCE(SUM(cp.quantite * cp.prix_unitaire), 0) as chiffre_affaires,
                COUNT(DISTINCT cp.commande_id) as nb_commandes_distinctes
            FROM produits p
            LEFT JOIN commande_produits cp ON p.id = cp.produit_id
            GROUP BY p.id, p.nom, p.prix, p.stock
            ORDER BY chiffre_affaires DESC
        """)
        
        return [dict(row) for row in cursor.fetchall()]
```

## 🎯 Démonstration complète
```python
def demo_boutique():
    """Démonstration complète du système"""
    boutique = BoutiqueBD()
    
    print("=== CRÉATION DES DONNÉES ===")
    
    # Ajouter des clients
    clients_data = [
        Client("Alice Martin", "alice@email.com", "0123456789", "1 rue de la Paix, Paris"),
        Client("Bob Durand", "bob@email.com", "0987654321", "5 avenue Victor Hugo, Lyon"),
        Client("Charlie Roy", "charlie@email.com", "0147258369", "10 boulevard Saint-Michel, Marseille")
    ]
    
    clients_ids = []
    for client in clients_data:
        client_id = boutique.ajouter_client(client)
        if client_id:
            clients_ids.append(client_id)
    
    # Ajouter des produits
    produits_data = [
        Produit("Ordinateur portable", 899.99, 10, "PC portable 15 pouces"),
        Produit("Souris sans fil", 29.99, 50, "Souris ergonomique"),
        Produit("Clavier mécanique", 129.99, 25, "Clavier gaming RGB"),
        Produit("Écran 4K", 399.99, 8, "Écran 27 pouces 4K")
    ]
    
    produits_ids = []
    for produit in produits_data:
        produit_id = boutique.ajouter_produit(produit)
        if produit_id:
            produits_ids.append(produit_id)
    
    print("\\n=== CRÉATION DE COMMANDES ===")
    
    # Commande pour Alice
    if clients_ids and produits_ids:
        commande1 = boutique.creer_commande(clients_ids[0])  # Alice
        if commande1:
            boutique.ajouter_produit_commande(commande1, produits_ids[0], 1)  # PC
            boutique.ajouter_produit_commande(commande1, produits_ids[1], 2)  # 2 souris
        
        # Commande pour Bob
        commande2 = boutique.creer_commande(clients_ids[1])  # Bob
        if commande2:
            boutique.ajouter_produit_commande(commande2, produits_ids[2], 1)  # Clavier
            boutique.ajouter_produit_commande(commande2, produits_ids[3], 1)  # Écran
    
    print("\\n=== ANALYSES AVEC JOINS ===")
    
    # Rapport des ventes
    rapport = boutique.rapport_ventes()
    print(f"📊 Total des ventes: {rapport['total_ventes']}€")
    print(f"📊 Nombre de commandes: {rapport['nombre_commandes']}")
    print(f"📊 Panier moyen: {rapport['panier_moyen']}€")
    
    if rapport['produit_top']:
        print(f"🏆 Produit top: {rapport['produit_top'][0]} ({rapport['produit_top'][1]} vendus)")
    
    if rapport['client_top']:
        print(f"🏆 Client top: {rapport['client_top'][0]} ({rapport['client_top'][2]}€)")
    
    # Statistiques par client
    print("\\n=== STATISTIQUES CLIENTS ===")
    stats_clients = boutique.statistiques_par_client()
    for stat in stats_clients:
        print(f"👤 {stat['nom']}: {stat['nb_commandes']} commandes, {stat['total_achats']}€")
    
    # Clients sans commande
    sans_commande = boutique.clients_sans_commande()
    if sans_commande:
        print("\\n⚠️ Clients sans commande:")
        for client in sans_commande:
            print(f"  - {client['nom']} ({client['email']})")

if __name__ == "__main__":
    demo_boutique()
```

Les **JOINs** permettent de combiner les données de plusieurs tables pour créer des rapports puissants ! 

**Suite dans la Partie 2B** : APIs et requêtes HTTP ! 🌐''',
                    'code_exemple': '''# Exemple complet : Système de réservation d'hôtel

import sqlite3
from datetime import date, datetime, timedelta
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from enum import Enum

class StatutReservation(Enum):
    CONFIRMEE = "confirmee"
    ANNULEE = "annulee"
    EN_ATTENTE = "en_attente"
    TERMINEE = "terminee"

class TypeChambre(Enum):
    SIMPLE = "simple"
    DOUBLE = "double"
    SUITE = "suite"

@dataclass
class Client:
    nom: str
    prenom: str
    email: str
    telephone: str
    adresse: str = None
    date_naissance: date = None
    id: Optional[int] = None

@dataclass
class Chambre:
    numero: str
    type_chambre: TypeChambre
    prix_nuit: float
    capacite_max: int
    description: str = None
    equipements: List[str] = field(default_factory=list)
    id: Optional[int] = None

@dataclass
class Reservation:
    client_id: int
    chambre_id: int
    date_arrivee: date
    date_depart: date
    nb_personnes: int
    prix_total: float = 0.0
    statut: StatutReservation = StatutReservation.EN_ATTENTE
    commentaires: str = None
    id: Optional[int] = None

class HotelDB:
    """Système de gestion d'hôtel avec relations avancées"""
    
    def __init__(self, db_name="hotel.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialise la base de données avec toutes les relations"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Activer les clés étrangères
            cursor.execute("PRAGMA foreign_keys = ON")
            
            # Table des clients
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    telephone TEXT NOT NULL,
                    adresse TEXT,
                    date_naissance DATE,
                    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    nb_sejours INTEGER DEFAULT 0,
                    total_depense REAL DEFAULT 0
                )
            """)
            
            # Table des chambres
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS chambres (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero TEXT UNIQUE NOT NULL,
                    type_chambre TEXT NOT NULL CHECK(type_chambre IN ('simple', 'double', 'suite')),
                    prix_nuit REAL NOT NULL CHECK(prix_nuit > 0),
                    capacite_max INTEGER NOT NULL CHECK(capacite_max > 0),
                    description TEXT,
                    equipements TEXT, -- JSON string
                    disponible BOOLEAN DEFAULT 1,
                    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Table des réservations
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    chambre_id INTEGER NOT NULL,
                    date_arrivee DATE NOT NULL,
                    date_depart DATE NOT NULL,
                    nb_personnes INTEGER NOT NULL CHECK(nb_personnes > 0),
                    prix_total REAL NOT NULL CHECK(prix_total >= 0),
                    statut TEXT DEFAULT 'en_attente' CHECK(statut IN ('confirmee', 'annulee', 'en_attente', 'terminee')),
                    commentaires TEXT,
                    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE,
                    FOREIGN KEY (chambre_id) REFERENCES chambres (id) ON DELETE CASCADE,
                    CHECK (date_depart > date_arrivee)
                )
            """)
            
            # Table des services additionnels
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    description TEXT,
                    prix REAL NOT NULL CHECK(prix >= 0),
                    categorie TEXT DEFAULT 'autre'
                )
            """)
            
            # Table de liaison réservation-services (N:N)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservation_services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    reservation_id INTEGER NOT NULL,
                    service_id INTEGER NOT NULL,
                    quantite INTEGER DEFAULT 1 CHECK(quantite > 0),
                    prix_unitaire REAL NOT NULL,
                    FOREIGN KEY (reservation_id) REFERENCES reservations (id) ON DELETE CASCADE,
                    FOREIGN KEY (service_id) REFERENCES services (id) ON DELETE CASCADE,
                    UNIQUE(reservation_id, service_id)
                )
            """)
            
            # Index pour optimiser les requêtes
            indexes = [
                "CREATE INDEX IF NOT EXISTS idx_clients_email ON clients(email)",
                "CREATE INDEX IF NOT EXISTS idx_chambres_type ON chambres(type_chambre)",
                "CREATE INDEX IF NOT EXISTS idx_reservations_dates ON reservations(date_arrivee, date_depart)",
                "CREATE INDEX IF NOT EXISTS idx_reservations_client ON reservations(client_id)",
                "CREATE INDEX IF NOT EXISTS idx_reservations_chambre ON reservations(chambre_id)",
                "CREATE INDEX IF NOT EXISTS idx_reservations_statut ON reservations(statut)"
            ]
            
            for index in indexes:
                cursor.execute(index)
            
            conn.commit()
            print("✅ Base de données hôtel initialisée")
    
    def ajouter_client(self, client: Client) -> Optional[int]:
        """Ajoute un nouveau client"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO clients (nom, prenom, email, telephone, adresse, date_naissance)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (client.nom, client.prenom, client.email, client.telephone, 
                      client.adresse, client.date_naissance))
                
                client_id = cursor.lastrowid
                conn.commit()
                print(f"✅ Client {client.prenom} {client.nom} ajouté (ID: {client_id})")
                return client_id
        except sqlite3.IntegrityError:
            print(f"❌ Email {client.email} déjà utilisé")
            return None
    
    def ajouter_chambre(self, chambre: Chambre) -> Optional[int]:
        """Ajoute une nouvelle chambre"""
        try:
            import json
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO chambres (numero, type_chambre, prix_nuit, capacite_max, description, equipements)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (chambre.numero, chambre.type_chambre.value, chambre.prix_nuit, 
                      chambre.capacite_max, chambre.description, json.dumps(chambre.equipements)))
                
                chambre_id = cursor.lastrowid
                conn.commit()
                print(f"✅ Chambre {chambre.numero} ajoutée (ID: {chambre_id})")
                return chambre_id
        except sqlite3.IntegrityError:
            print(f"❌ Numéro de chambre {chambre.numero} déjà utilisé")
            return None
    
    def chambres_disponibles(self, date_arrivee: date, date_depart: date, nb_personnes: int = 1) -> List[Dict]:
        """Trouve les chambres disponibles pour une période"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT c.* 
                FROM chambres c
                WHERE c.disponible = 1 
                  AND c.capacite_max >= ?
                  AND c.id NOT IN (
                      SELECT DISTINCT r.chambre_id
                      FROM reservations r
                      WHERE r.statut IN ('confirmee', 'en_attente')
                        AND NOT (r.date_depart <= ? OR r.date_arrivee >= ?)
                  )
                ORDER BY c.prix_nuit
            """, (nb_personnes, date_arrivee, date_depart))
            
            return [dict(row) for row in cursor.fetchall()]
    
    def creer_reservation(self, reservation: Reservation) -> Optional[int]:
        """Crée une nouvelle réservation"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Vérifier disponibilité
                disponibles = self.chambres_disponibles(
                    reservation.date_arrivee, 
                    reservation.date_depart, 
                    reservation.nb_personnes
                )
                
                if not any(ch['id'] == reservation.chambre_id for ch in disponibles):
                    print("❌ Chambre non disponible pour cette période")
                    return None
                
                # Calculer le prix
                cursor.execute("SELECT prix_nuit FROM chambres WHERE id = ?", (reservation.chambre_id,))
                prix_nuit = cursor.fetchone()[0]
                
                nb_nuits = (reservation.date_depart - reservation.date_arrivee).days
                prix_total = prix_nuit * nb_nuits
                
                # Créer la réservation
                cursor.execute("""
                    INSERT INTO reservations (client_id, chambre_id, date_arrivee, date_depart, 
                                            nb_personnes, prix_total, statut, commentaires)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (reservation.client_id, reservation.chambre_id, reservation.date_arrivee,
                      reservation.date_depart, reservation.nb_personnes, prix_total,
                      reservation.statut.value, reservation.commentaires))
                
                reservation_id = cursor.lastrowid
                conn.commit()
                print(f"✅ Réservation {reservation_id} créée ({nb_nuits} nuits, {prix_total}€)")
                return reservation_id
                
        except Exception as e:
            print(f"❌ Erreur création réservation: {e}")
            return None
    
    def reservations_client(self, client_id: int) -> List[Dict]:
        """Récupère toutes les réservations d'un client"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT 
                    r.id,
                    r.date_arrivee,
                    r.date_depart,
                    r.nb_personnes,
                    r.prix_total,
                    r.statut,
                    r.commentaires,
                    c.numero as numero_chambre,
                    c.type_chambre,
                    cl.nom,
                    cl.prenom
                FROM reservations r
                INNER JOIN chambres c ON r.chambre_id = c.id
                INNER JOIN clients cl ON r.client_id = cl.id
                WHERE r.client_id = ?
                ORDER BY r.date_arrivee DESC
            """, (client_id,))
            
            return [dict(row) for row in cursor.fetchall()]
    
    def planning_chambres(self, date_debut: date, date_fin: date) -> Dict:
        """Planning des chambres sur une période"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Réservations sur la période
            cursor.execute("""
                SELECT 
                    r.date_arrivee,
                    r.date_depart,
                    r.statut,
                    c.numero,
                    c.type_chambre,
                    cl.nom,
                    cl.prenom
                FROM reservations r
                INNER JOIN chambres c ON r.chambre_id = c.id
                INNER JOIN clients cl ON r.client_id = cl.id
                WHERE r.statut IN ('confirmee', 'en_attente')
                  AND NOT (r.date_depart <= ? OR r.date_arrivee >= ?)
                ORDER BY c.numero, r.date_arrivee
            """, (date_debut, date_fin))
            
            reservations = [dict(row) for row in cursor.fetchall()]
            
            # Taux d'occupation
            cursor.execute("""
                SELECT 
                    COUNT(DISTINCT c.id) as total_chambres,
                    COUNT(DISTINCT r.chambre_id) as chambres_occupees
                FROM chambres c
                LEFT JOIN reservations r ON c.id = r.chambre_id 
                    AND r.statut IN ('confirmee', 'en_attente')
                    AND NOT (r.date_depart <= ? OR r.date_arrivee >= ?)
            """, (date_debut, date_fin))
            
            taux = cursor.fetchone()
            taux_occupation = (taux['chambres_occupees'] / taux['total_chambres']) * 100 if taux['total_chambres'] > 0 else 0
            
            return {
                'reservations': reservations,
                'taux_occupation': round(taux_occupation, 1),
                'chambres_total': taux['total_chambres'],
                'chambres_occupees': taux['chambres_occupees']
            }
    
    def rapport_financier(self, annee: int = None) -> Dict:
        """Rapport financier détaillé"""
        if annee is None:
            annee = datetime.now().year
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Chiffre d'affaires par mois
            cursor.execute("""
                SELECT 
                    strftime('%m', date_arrivee) as mois,
                    COUNT(*) as nb_reservations,
                    SUM(prix_total) as ca_mois,
                    AVG(prix_total) as panier_moyen
                FROM reservations
                WHERE strftime('%Y', date_arrivee) = ?
                  AND statut IN ('confirmee', 'terminee')
                GROUP BY strftime('%m', date_arrivee)
                ORDER BY mois
            """, (str(annee),))
            
            ca_mensuel = cursor.fetchall()
            
            # Top clients
            cursor.execute("""
                SELECT 
                    cl.nom,
                    cl.prenom,
                    cl.email,
                    COUNT(r.id) as nb_sejours,
                    SUM(r.prix_total) as total_depense,
                    AVG(r.prix_total) as sejour_moyen
                FROM clients cl
                INNER JOIN reservations r ON cl.id = r.client_id
                WHERE strftime('%Y', r.date_arrivee) = ?
                  AND r.statut IN ('confirmee', 'terminee')
                GROUP BY cl.id
                ORDER BY total_depense DESC
                LIMIT 10
            """, (str(annee),))
            
            top_clients = cursor.fetchall()
            
            # Performance des chambres
            cursor.execute("""
                SELECT 
                    c.numero,
                    c.type_chambre,
                    c.prix_nuit,
                    COUNT(r.id) as nb_reservations,
                    SUM(r.prix_total) as ca_chambre,
                    ROUND(
                        COUNT(r.id) * 100.0 / 
                        (julianday(?) - julianday(?) + 1), 2
                    ) as taux_occupation
                FROM chambres c
                LEFT JOIN reservations r ON c.id = r.chambre_id 
                    AND strftime('%Y', r.date_arrivee) = ?
                    AND r.statut IN ('confirmee', 'terminee')
                GROUP BY c.id
                ORDER BY ca_chambre DESC
            """, (f"{annee}-12-31", f"{annee}-01-01", str(annee)))
            
            perf_chambres = cursor.fetchall()
            
            return {
                'annee': annee,
                'ca_mensuel': ca_mensuel,
                'top_clients': top_clients,
                'performance_chambres': perf_chambres
            }
    
    def clients_fideles(self) -> List[Dict]:
        """Identifie les clients fidèles"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT 
                    cl.id,
                    cl.nom,
                    cl.prenom,
                    cl.email,
                    COUNT(r.id) as nb_sejours,
                    SUM(r.prix_total) as total_depense,
                    MIN(r.date_arrivee) as premier_sejour,
                    MAX(r.date_arrivee) as dernier_sejour,
                    AVG(r.prix_total) as sejour_moyen
                FROM clients cl
                INNER JOIN reservations r ON cl.id = r.client_id
                WHERE r.statut IN ('confirmee', 'terminee')
                GROUP BY cl.id
                HAVING COUNT(r.id) >= 3 OR SUM(r.prix_total) >= 1000
                ORDER BY nb_sejours DESC, total_depense DESC
            """)
            
            return [dict(row) for row in cursor.fetchall()]

def demo_hotel():
    """Démonstration complète du système hôtel"""
    hotel = HotelDB()
    
    print("=== CRÉATION DES DONNÉES DE TEST ===")
    
    # Clients
    clients = [
        Client("Dupont", "Jean", "jean.dupont@email.com", "0123456789", "1 rue de la Paix, Paris"),
        Client("Martin", "Sophie", "sophie.martin@email.com", "0987654321", "5 av Victor Hugo, Lyon"),
        Client("Durand", "Pierre", "pierre.durand@email.com", "0147258369", "10 bd Saint-Michel, Marseille")
    ]
    
    clients_ids = []
    for client in clients:
        client_id = hotel.ajouter_client(client)
        if client_id:
            clients_ids.append(client_id)
    
    # Chambres
    chambres = [
        Chambre("101", TypeChambre.SIMPLE, 89.0, 2, "Chambre simple vue jardin", ["wifi", "tv", "climatisation"]),
        Chambre("201", TypeChambre.DOUBLE, 129.0, 4, "Chambre double vue mer", ["wifi", "tv", "balcon", "minibar"]),
        Chambre("301", TypeChambre.SUITE, 299.0, 6, "Suite présidentielle", ["wifi", "tv", "jacuzzi", "service_room"])
    ]
    
    chambres_ids = []
    for chambre in chambres:
        chambre_id = hotel.ajouter_chambre(chambre)
        if chambre_id:
            chambres_ids.append(chambre_id)
    
    print("\\n=== RÉSERVATIONS ===")
    
    # Créer des réservations
    if clients_ids and chambres_ids:
        # Réservation 1
        res1 = Reservation(
            client_id=clients_ids[0],
            chambre_id=chambres_ids[1],
            date_arrivee=date(2024, 3, 15),
            date_depart=date(2024, 3, 18),
            nb_personnes=2,
            statut=StatutReservation.CONFIRMEE
        )
        hotel.creer_reservation(res1)
        
        # Réservation 2
        res2 = Reservation(
            client_id=clients_ids[1],
            chambre_id=chambres_ids[2],
            date_arrivee=date(2024, 3, 20),
            date_depart=date(2024, 3, 25),
            nb_personnes=4,
            statut=StatutReservation.CONFIRMEE
        )
        hotel.creer_reservation(res2)
    
    print("\\n=== ANALYSES AVEC JOINS ===")
    
    # Planning
    planning = hotel.planning_chambres(date(2024, 3, 1), date(2024, 3, 31))
    print(f"📊 Taux d'occupation Mars 2024: {planning['taux_occupation']}%")
    print(f"📊 Chambres occupées: {planning['chambres_occupees']}/{planning['chambres_total']}")
    
    # Clients fidèles
    fideles = hotel.clients_fideles()
    if fideles:
        print("\\n🏆 Clients fidèles:")
        for client in fideles:
            print(f"  {client['prenom']} {client['nom']}: {client['nb_sejours']} séjours, {client['total_depense']}€")
    
    # Rapport financier
    rapport = hotel.rapport_financier(2024)
    print(f"\\n💰 Rapport financier {rapport['annee']}:")
    print(f"Top client: {rapport['top_clients'][0] if rapport['top_clients'] else 'Aucun'}")

if __name__ == "__main__":
    demo_hotel()''',
                    'exercice': '''## 🎯 Exercice : Système de bibliothèque avec relations

**Objectif :** Créer un système complet de bibliothèque avec relations entre tables

### Partie 1 : Modélisation des relations

Créez un système avec ces entités et relations :

#### Tables principales
```sql
-- Auteurs
CREATE TABLE auteurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    date_naissance DATE,
    nationalite TEXT,
    biographie TEXT
);

-- Livres
CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    isbn TEXT UNIQUE,
    date_publication DATE,
    nombre_pages INTEGER,
    genre TEXT,
    resume TEXT,
    stock_total INTEGER DEFAULT 1,
    stock_disponible INTEGER DEFAULT 1
);

-- Relation N:N Livres-Auteurs
CREATE TABLE livre_auteurs (
    livre_id INTEGER,
    auteur_id INTEGER,
    role TEXT DEFAULT 'auteur', -- 'auteur', 'co-auteur', 'traducteur'
    PRIMARY KEY (livre_id, auteur_id),
    FOREIGN KEY (livre_id) REFERENCES livres (id),
    FOREIGN KEY (auteur_id) REFERENCES auteurs (id)
);

-- Membres
CREATE TABLE membres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telephone TEXT,
    adresse TEXT,
    date_inscription DATE DEFAULT (date('now')),
    type_membre TEXT DEFAULT 'standard', -- 'standard', 'premium', 'etudiant'
    actif BOOLEAN DEFAULT 1
);

-- Emprunts
CREATE TABLE emprunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    membre_id INTEGER NOT NULL,
    livre_id INTEGER NOT NULL,
    date_emprunt DATE DEFAULT (date('now')),
    date_retour_prevue DATE NOT NULL,
    date_retour_effective DATE,
    amende REAL DEFAULT 0,
    statut TEXT DEFAULT 'en_cours', -- 'en_cours', 'retourne', 'perdu'
    FOREIGN KEY (membre_id) REFERENCES membres (id),
    FOREIGN KEY (livre_id) REFERENCES livres (id)
);
```

### Partie 2 : Classes Python

```python
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import List, Optional, Dict
import sqlite3

@dataclass
class Auteur:
    nom: str
    prenom: str
    date_naissance: date = None
    nationalite: str = None
    biographie: str = None
    id: Optional[int] = None

@dataclass
class Livre:
    titre: str
    isbn: str = None
    date_publication: date = None
    nombre_pages: int = None
    genre: str = None
    resume: str = None
    stock_total: int = 1
    stock_disponible: int = 1
    id: Optional[int] = None

@dataclass
class Membre:
    nom: str
    prenom: str
    email: str
    telephone: str = None
    adresse: str = None
    type_membre: str = 'standard'
    actif: bool = True
    id: Optional[int] = None

@dataclass
class Emprunt:
    membre_id: int
    livre_id: int
    date_emprunt: date = None
    date_retour_prevue: date = None
    date_retour_effective: date = None
    amende: float = 0.0
    statut: str = 'en_cours'
    id: Optional[int] = None

class BibliothequeDB:
    def __init__(self, db_name="bibliotheque.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialise toutes les tables avec relations"""
        # À implémenter
        pass
    
    # === GESTION DES AUTEURS ===
    
    def ajouter_auteur(self, auteur: Auteur) -> Optional[int]:
        """Ajoute un auteur"""
        pass
    
    def rechercher_auteurs(self, terme: str) -> List[Dict]:
        """Recherche d'auteurs par nom/prénom"""
        pass
    
    # === GESTION DES LIVRES ===
    
    def ajouter_livre(self, livre: Livre, auteurs_ids: List[int]) -> Optional[int]:
        """Ajoute un livre avec ses auteurs"""
        pass
    
    def livres_par_auteur(self, auteur_id: int) -> List[Dict]:
        """Tous les livres d'un auteur avec JOINs"""
        pass
    
    def livres_disponibles(self, genre: str = None) -> List[Dict]:
        """Livres disponibles à l'emprunt"""
        pass
    
    def rechercher_livres(self, terme: str) -> List[Dict]:
        """Recherche par titre, auteur, ISBN"""
        pass
    
    # === GESTION DES MEMBRES ===
    
    def inscrire_membre(self, membre: Membre) -> Optional[int]:
        """Inscrit un nouveau membre"""
        pass
    
    def membres_actifs(self) -> List[Dict]:
        """Liste des membres actifs"""
        pass
    
    # === GESTION DES EMPRUNTS ===
    
    def emprunter_livre(self, membre_id: int, livre_id: int, duree_jours: int = 14) -> Optional[int]:
        """Crée un emprunt"""
        # Vérifications :
        # - Livre disponible
        # - Membre actif
        # - Limite d'emprunts par membre
        pass
    
    def retourner_livre(self, emprunt_id: int) -> bool:
        """Retourne un livre"""
        # Calculer les amendes si retard
        pass
    
    def emprunts_membre(self, membre_id: int, actifs_seulement: bool = False) -> List[Dict]:
        """Emprunts d'un membre avec détails livre/auteur"""
        pass
    
    def emprunts_en_retard(self) -> List[Dict]:
        """Emprunts en retard avec JOINs"""
        pass
    
    # === STATISTIQUES AVANCÉES ===
    
    def top_livres_empruntes(self, limite: int = 10) -> List[Dict]:
        """Livres les plus empruntés"""
        pass
    
    def top_auteurs_populaires(self, limite: int = 10) -> List[Dict]:
        """Auteurs les plus empruntés"""
        pass
    
    def membres_les_plus_actifs(self, limite: int = 10) -> List[Dict]:
        """Membres avec le plus d'emprunts"""
        pass
    
    def rapport_genre(self) -> List[Dict]:
        """Statistiques par genre de livre"""
        pass
    
    def evolution_emprunts_mensuelle(self, annee: int) -> List[Dict]:
        """Évolution mensuelle des emprunts"""
        pass
```

### Partie 3 : Requêtes JOIN avancées

Implémentez ces requêtes complexes :

#### A. Catalogue complet avec auteurs
```sql
SELECT 
    l.titre,
    l.isbn,
    l.genre,
    l.stock_disponible,
    GROUP_CONCAT(a.prenom || ' ' || a.nom, ', ') as auteurs
FROM livres l
LEFT JOIN livre_auteurs la ON l.id = la.livre_id
LEFT JOIN auteurs a ON la.auteur_id = a.id
GROUP BY l.id
ORDER BY l.titre;
```

#### B. Membres avec leurs statistiques d'emprunt
```sql
SELECT 
    m.prenom || ' ' || m.nom as nom_complet,
    m.email,
    m.type_membre,
    COUNT(e.id) as total_emprunts,
    COUNT(CASE WHEN e.statut = 'en_cours' THEN 1 END) as emprunts_actuels,
    COALESCE(SUM(e.amende), 0) as total_amendes,
    MAX(e.date_emprunt) as dernier_emprunt
FROM membres m
LEFT JOIN emprunts e ON m.id = e.membre_id
WHERE m.actif = 1
GROUP BY m.id
ORDER BY total_emprunts DESC;
```

#### C. Auteurs avec leur productivité
```sql
SELECT 
    a.prenom || ' ' || a.nom as auteur,
    a.nationalite,
    COUNT(DISTINCT l.id) as nb_livres,
    COUNT(e.id) as total_emprunts,
    AVG(l.nombre_pages) as pages_moyennes
FROM auteurs a
LEFT JOIN livre_auteurs la ON a.id = la.auteur_id
LEFT JOIN livres l ON la.livre_id = l.id
LEFT JOIN emprunts e ON l.id = e.livre_id
GROUP BY a.id
HAVING COUNT(DISTINCT l.id) > 0
ORDER BY nb_livres DESC, total_emprunts DESC;
```

### Partie 4 : Analyses et rapports

#### A. Tableau de bord de la bibliothèque
```python
def tableau_de_bord(self) -> Dict:
    """Indicateurs clés de performance"""
    # Implémenter :
    # - Nombre total de livres/membres
    # - Taux d'occupation des livres
    # - Moyenne d'emprunts par membre
    # - Top 5 genres les plus populaires
    # - Amendes impayées
    pass
```

#### B. Recommandations de livres
```python
def recommander_livres(self, membre_id: int, limite: int = 5) -> List[Dict]:
    """Recommande des livres basé sur l'historique"""
    # Logique :
    # - Analyser les genres préférés du membre
    # - Trouver des livres similaires non empruntés
    # - Privilégier les livres populaires
    pass
```

#### C. Gestion des stocks
```python
def livres_populaires_faible_stock(self) -> List[Dict]:
    """Identifie les livres à racheter"""
    # Livres très empruntés mais avec peu de stock
    pass

def livres_jamais_empruntes(self) -> List[Dict]:
    """Livres qui ne sortent jamais"""
    pass
```

### Partie 5 : Interface utilisateur

Créez un menu avec :

1. **Gestion du catalogue**
   - Ajouter livre/auteur
   - Recherche multicritères
   - Gestion des stocks

2. **Gestion des membres**
   - Inscription/modification
   - Historique des emprunts
   - Gestion des amendes

3. **Emprunts/Retours**
   - Nouvel emprunt
   - Retour de livre
   - Prolongation

4. **Rapports et analyses**
   - Tableau de bord
   - Statistiques détaillées
   - Export des données

### Partie 6 : Données de test

```python
def creer_donnees_test():
    """Crée un jeu de données réalistes"""
    # 20+ auteurs variés
    # 100+ livres de différents genres
    # 50+ membres actifs
    # 200+ emprunts historiques
    pass
```

### Fonctionnalités bonus

1. **Réservations** : Système de réservation pour livres empruntés
2. **Notifications** : Rappels de retour par email
3. **Code-barres** : Gestion par scan de codes
4. **Multi-bibliothèques** : Réseau de bibliothèques
5. **API REST** : Interface pour applications mobiles
6. **Statistiques avancées** : Analyses prédictives
7. **Import/Export** : Intégration avec autres systèmes

### Critères de réussite

- ✅ Relations bien modélisées et contraintes respectées
- ✅ Requêtes JOIN optimisées et performantes  
- ✅ Gestion complète du cycle de vie des emprunts
- ✅ Statistiques pertinentes et actionables
- ✅ Interface utilisateur complète et intuitive
- ✅ Performance correcte avec 10 000+ livres
- ✅ Intégrité des données garantie

**Challenge :** Le système doit gérer une vraie bibliothèque avec des milliers de livres et centaines de membres ! 📚'''
                }
            )

        # Cours 4: Python Expert (renommé et réordonné)  
        cours_expert, created = Cours.objects.get_or_create(
            slug='python-expert',
            defaults={
                'titre': 'Python Expert',
                'description': 'Maîtrisez les concepts avancés de Python : décorateurs, générateurs, métaclasses, programmation asynchrone et optimisation de performances.',
                'niveau': 'expert',
                'duree_estimee': 20,
                'ordre': 4,
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