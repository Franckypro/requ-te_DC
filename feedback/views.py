# feedback/views.py

from django.shortcuts import render, redirect
from .forms import RetourForm
from .models import Retour
from django.http import HttpResponse


def accueil(request):
    return render(request, 'feedback/accueil.html')

def soumettre_retour(request):
    if request.method == 'POST':
        form = RetourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('confirmation')  # Redirige vers la page de confirmation
        else:
            return HttpResponse("Erreur lors de la soumission du formulaire")
    else:
        form = RetourForm()
    
    return render(request, 'feedback/soumettre_retour.html', {'form': form})

def confirmation(request):
    return render(request, 'feedback/confirmation.html')

def liste_retours(request):
    # Récupérer les options de "formation" dynamiquement depuis les données existantes
    formations = Retour.objects.values_list('formation', flat=True).distinct()
    
    # Récupération des filtres
    date_debut = request.GET.get('date_debut')
    date_fin = request.GET.get('date_fin')
    sujet = request.GET.get('sujet')
    
    # Filtrer les retours en fonction des critères
    retours = Retour.objects.all()
    if date_debut:
        retours = retours.filter(date__gte=date_debut)
    if date_fin:
        retours = retours.filter(date__lte=date_fin)
    if sujet:
        retours = retours.filter(formation=sujet)
    
    # Ajout de la pagination si nécessaire
    from django.core.paginator import Paginator
    paginator = Paginator(retours, 10)  # 10 éléments par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'retours': page_obj,  # Objets paginés
        'formations': formations,  # Options disponibles pour le champ "sujet"
        'is_paginated': paginator.num_pages > 1,
        'page_obj': page_obj,
    }
    return render(request, 'feedback/liste_retours.html', context)