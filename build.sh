#!/bin/bash
set -e

echo "🚀 Début du build Railway..."

# Installation des dépendances
echo "📦 Installation des dépendances..."
pip install --upgrade pip
pip install -r requirements.txt

# Collecte des fichiers statiques
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --clear

# Migrations
echo "🗄️ Application des migrations..."
python manage.py migrate --noinput

echo "✅ Build terminé avec succès!"