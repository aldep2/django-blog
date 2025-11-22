#!/usr/bin/env bash
# Script de déploiement Railway

echo "🚀 Démarrage du déploiement Railway..."

# Collecter les fichiers statiques
echo "📦 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

# Appliquer les migrations
echo "🗄️ Application des migrations..."
python manage.py migrate --noinput

# Créer le superutilisateur si défini
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    echo "👤 Création du superutilisateur..."
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
    print('✅ Superutilisateur créé')
else:
    print('ℹ️ Superutilisateur existe déjà')
"
fi

# Peupler le blog si demandé
if [ "$POPULATE_BLOG" = "true" ]; then
    echo "📝 Peuplement du blog avec des données d'exemple..."
    python manage.py populate_blog
fi

echo "✅ Déploiement terminé !"