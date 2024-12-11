from django.test import TestCase
from .models import Apprenant, Retour

class RetourTests(TestCase):
    def test_soumettre_retour(self):
        apprenant = Apprenant.objects.create(nom='John Doe', email='john@example.com')
        response = self.client.post('/soumettre/', {'apprenant': apprenant.id, 'note': 5, 'commentaire': 'Excellent bootcamp!'})
        self.assertEqual(response.status_code, 302)  # Redirection après soumission
        self.assertEqual(Retour.objects.count(), 1)
