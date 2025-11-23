from django.contrib import admin
from django.utils.html import format_html
from .models import Categorie, Article, Commentaire, Cours, Chapitre


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


class ChapitreInline(admin.TabularInline):
    """Inline pour gérer les chapitres depuis l'interface cours"""
    model = Chapitre
    extra = 1
    fields = ['ordre', 'titre', 'slug']
    prepopulated_fields = {'slug': ('titre',)}


@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    """Administration des cours"""
    list_display = ['titre', 'niveau', 'duree_estimee', 'nombre_chapitres', 'actif', 'ordre']
    list_filter = ['niveau', 'actif', 'date_creation']
    search_fields = ['titre', 'description']
    prepopulated_fields = {'slug': ('titre',)}
    list_editable = ['actif', 'ordre']
    
    inlines = [ChapitreInline]
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('titre', 'slug', 'description', 'image')
        }),
        ('Paramètres du cours', {
            'fields': ('niveau', 'duree_estimee', 'ordre', 'actif')
        }),
    )
    
    def nombre_chapitres(self, obj):
        """Affiche le nombre de chapitres"""
        return obj.chapitres.count()
    nombre_chapitres.short_description = 'Chapitres'


@admin.register(Chapitre)
class ChapitreAdmin(admin.ModelAdmin):
    """Administration des chapitres"""
    list_display = ['cours', 'titre', 'ordre', 'a_code_exemple', 'a_exercice', 'date_creation']
    list_filter = ['cours', 'date_creation']
    search_fields = ['titre', 'contenu', 'cours__titre']
    prepopulated_fields = {'slug': ('titre',)}
    list_editable = ['ordre']
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('cours', 'titre', 'slug', 'ordre')
        }),
        ('Contenu', {
            'fields': ('contenu', 'code_exemple', 'exercice')
        }),
    )
    
    def a_code_exemple(self, obj):
        """Indique si le chapitre a un code d'exemple"""
        return bool(obj.code_exemple)
    a_code_exemple.boolean = True
    a_code_exemple.short_description = 'Code exemple'
    
    def a_exercice(self, obj):
        """Indique si le chapitre a un exercice"""
        return bool(obj.exercice)
    a_exercice.boolean = True
    a_exercice.short_description = 'Exercice'


# Configuration du site d'administration
admin.site.site_header = "Administration du Blog & Cours"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Bienvenue dans l'administration du blog et des cours"