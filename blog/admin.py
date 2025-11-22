from django.contrib import admin
from django.utils.html import format_html
from .models import Categorie, Article, Commentaire


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    """Administration des catégories"""
    list_display = ['nom', 'couleur_display', 'description']
    search_fields = ['nom', 'description']
    prepopulated_fields = {}
    
    def couleur_display(self, obj):
        return format_html(
            '<span style="color: {}; font-weight: bold;">● {}</span>',
            obj.couleur,
            obj.couleur
        )
    couleur_display.short_description = 'Couleur'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Administration des articles"""
    list_display = ['titre', 'auteur', 'categorie', 'statut', 'date_publication', 'vues']
    list_filter = ['statut', 'categorie', 'date_creation', 'auteur']
    search_fields = ['titre', 'contenu']
    prepopulated_fields = {'slug': ('titre',)}
    date_hierarchy = 'date_publication'
    list_editable = ['statut']
    
    fieldsets = (
        ('Contenu', {
            'fields': ('titre', 'slug', 'categorie', 'extrait', 'contenu', 'image')
        }),
        ('Métadonnées', {
            'fields': ('auteur', 'statut', 'date_publication'),
            'classes': ('collapse',)
        }),
        ('Statistiques', {
            'fields': ('vues',),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Assigne automatiquement l'auteur à l'utilisateur connecté"""
        if not change:  # Si c'est un nouvel article
            obj.auteur = request.user
        super().save_model(request, obj, form, change)


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    """Administration des commentaires"""
    list_display = ['article', 'auteur', 'extrait_contenu', 'date_creation', 'actif']
    list_filter = ['actif', 'date_creation', 'article']
    search_fields = ['contenu', 'auteur__username', 'article__titre']
    list_editable = ['actif']
    date_hierarchy = 'date_creation'
    
    def extrait_contenu(self, obj):
        """Affiche un extrait du contenu du commentaire"""
        return obj.contenu[:50] + '...' if len(obj.contenu) > 50 else obj.contenu
    extrait_contenu.short_description = 'Contenu'


# Configuration du site d'administration
admin.site.site_header = "Administration du Blog"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Bienvenue dans l'administration du blog"