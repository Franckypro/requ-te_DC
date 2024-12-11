# feedback/forms.py

from django import forms
from .models import Retour

class RetourForm(forms.ModelForm):
    class Meta:
        model = Retour
        fields = ['formation', 'prioriteRetour', 'typeRetour', 'rating', 'comments', 'attachedfiles', 'consentement']
