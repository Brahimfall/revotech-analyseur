# Dans views.py
from django.shortcuts import render, redirect

from .form import AuteurForm
from .models import Auteur


def acceuil(request):
    auteurs = Auteur.objects.all()
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acceuil')  # Rediriger vers la même page après soumission du formulaire
    else:
        form = AuteurForm()

    context = {'auteurs': auteurs, 'form': form}
    return render(request, 'index.html', context)
