from django.contrib import admin

# Register your models here.
from .models import Videojuego,Analisis,Estudio,Plataforma,Sede 

admin.site.register(Videojuego)
admin.site.register(Analisis)
admin.site.register(Estudio)
admin.site.register(Plataforma)
admin.site.register(Sede) 