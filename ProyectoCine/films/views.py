from django.shortcuts import render
from .models import age,film,gener
# Create your views here.

def show(request):

    peliculas = film.objects.all()

    nueva_lista = [peliculas[i:i+4] for i in range(0, len(peliculas), 4)]
    
    
    return render(request,'showfilms.html',{
        "peliculas":nueva_lista,
        "title": "Peliculas"
    })