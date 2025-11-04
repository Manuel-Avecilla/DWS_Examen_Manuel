from django.db import models

# Create your models here.

#------------------------------- Plataforma ------------------------------------------ 
class Plataforma(models.Model): 
    nombre = models.CharField(max_length=150)
    fabricante = models.CharField(max_length=150)
    
#------------------------------- Estudio ------------------------------------------ 
class Estudio(models.Model):
    nombre = models.CharField(max_length=150) #inventado
    

#------------------------------- Videojuego ------------------------------------------ 
class Videojuego(models.Model): 

    estudio_desarrollo = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='videojuegoEstudio')
    plataforma = models.ManyToManyField(Plataforma, blank=True, related_name='videojuegoPlataforma')
    
    titulo = models.CharField(max_length=150)
    ventas_estimadas = models.PositiveIntegerField()

#------------------------------- Sede ------------------------------------------ 
class Sede(models.Model):
    estudio_id = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='sedeEstudio')
    
    pais = models.CharField(max_length=150)

#------------------------------- Analisis ------------------------------------------ 
class Analisis(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE, related_name='analisisVideojuego')
    
    puntuacion = models.PositiveIntegerField()
    fecha_analisis = models.DateField(null=True, blank=True)
    critico = models.CharField(max_length=150)
