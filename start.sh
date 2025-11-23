#!/bin/bash
set -e

echo "🚀 Démarrage de l'application Django sur Railway..."

# Appliquer les migrations
echo "📊 Application des migrations..."
python manage.py migrate --noinput

# Collecter les fichiers statiques
echo "📁 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --clear

# Peupler le blog si la variable est définie
if [ "$POPULATE_BLOG" = "true" ]; then
    echo "📝 Peuplement du blog avec des données d'exemple..."
    python manage.py populate_blog
fi

# Démarrer le serveur Gunicorn
echo "🌐 Démarrage du serveur web..."
gunicorn monprojet.wsgi:application --bind 0.0.0.0:$PORT