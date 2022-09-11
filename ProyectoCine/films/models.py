from django.db import models

# Create your models here.

class gener(models.Model):
    name = models.CharField(max_length=100,verbose_name="Genero")
    description = models.CharField(max_length=1000,verbose_name="Descripcion del genero")
    
     
    class Meta:
        verbose_name="Genero"
        verbose_name_plural = "Generos"
     
    def __str__(self):
        return self.name
    


class age(models.Model):
    clasificacion = models.CharField(max_length=20,verbose_name="Clasificacion")

    class Meta:
        verbose_name="Edad Permitida"
        verbose_name_plural = "Edades Permitidas"
    
    def __str__(self):
        return self.clasificacion

class film(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nombre")
    duration = models.CharField(max_length=4,verbose_name="Duracion")
    image = models.ImageField(default=None)
    realese_date = models.TimeField(verbose_name="Fecha de Estreno")
    clasification = models.ForeignKey("age",on_delete=models.CASCADE,verbose_name="Clasificacion")
    genero = models.ForeignKey("gener", on_delete=models.CASCADE,verbose_name="Genero")
    link = models.CharField(verbose_name="Trailer", default=None,max_length=1000)
    abstract = models.TextField(verbose_name="Resumen")

     
    class Meta:
        verbose_name="Pelicula"
        verbose_name_plural = "Peliculas"

    def __str__(self):
        return self.name