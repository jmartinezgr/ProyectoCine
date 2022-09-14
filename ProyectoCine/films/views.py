from django.shortcuts import render,redirect
from .models import age,film,gener
# Create your views here.

def show(request):

    peliculas = film.objects.all()  

    nueva_lista = [peliculas[i:i+4] for i in range(0, len(peliculas), 4)]
    
    
    return render(request,'showfilms.html',{
        "peliculas":nueva_lista,
        "title": "Peliculas"
    })

def one_film(request,name):
    try:
        pelicula = film.objects.get(name=name)
        id = pelicula.id
        genero = film.genero.through.objects.filter(film_id=id).values_list('gener_id')
        genero = gener.objects.filter(id__in=genero).values_list('name',flat=True)
    
        return render(request,'showonefilm.html',{
            "genero":genero,
            "pelicula":pelicula
        })
    except:
        return redirect('/peliculas/')

    