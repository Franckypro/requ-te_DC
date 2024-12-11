# feedback/models.py

from django.db import models

class Retour(models.Model):
    formation = models.CharField(max_length=200)
    prioriteRetour = models.CharField(max_length=100)
    typeRetour = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    comments = models.TextField(blank=True, null=True)
    attachedfiles = models.FileField(upload_to='feedback/', blank=True, null=True)
    consentement = models.BooleanField(default=False)

    def __str__(self):
        return f"Retour sur {self.formation} - {self.rating} étoiles"
