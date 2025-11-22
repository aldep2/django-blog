from django import forms
from .models import Commentaire


class CommentaireForm(forms.ModelForm):
    """Formulaire pour les commentaires"""
    
    class Meta:
        model = Commentaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Écrivez votre commentaire ici...',
                'maxlength': '500'
            }),
        }
        labels = {
            'contenu': 'Votre commentaire',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contenu'].required = True