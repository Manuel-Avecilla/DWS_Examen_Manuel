from django.shortcuts import render
from django.views.defaults import page_not_found
from django.db.models import Q , Prefetch, Avg, Max, Min
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

#------------------------------------------------------------------------------------------

def dame_videojuegos_titulo_pais(request, titulo, pais):
    
    videojuegos = (
        Videojuego.objects
        .select_related("estudio_desarrollo")
        .prefetch_related("plataforma", "estudio_desarrollo__sedeEstudio")
        .filter(titulo__contains = titulo, estudio_desarrollo__sedeEstudio__pais__contains = pais)
        .all()
    )
    
    return render(request,'lista_videojuegos.html',{'Videojuegos_Mostrar':videojuegos})

#------------------------------------------------------------------------------------------

def dame_videojuegos_buenos(request, fabricante,nombre_plataforma,puntuacion):
    
    videojuegos = (
        Videojuego.objects
        .select_related("estudio_desarrollo")
        .prefetch_related("plataforma", "estudio_desarrollo__sedeEstudio")
        .filter(Q(plataforma__fabricante__contains = fabricante)|Q(plataforma__nombre__contains = nombre_plataforma))
        .filter(analisisVideojuego__puntuacion__gt=puntuacion)
        .all()
        .distinct()
    )
    
    return render(request,'lista_videojuegos.html',{'Videojuegos_Mostrar':videojuegos})

#------------------------------------------------------------------------------------------

def dame_videojuegos_sin_plataformas(request):
    
    videojuegos = (
        Videojuego.objects
        .select_related("estudio_desarrollo")
        .prefetch_related("plataforma", "estudio_desarrollo__sedeEstudio")
        .filter(plataforma = None)
        .all()
    )
    
    return render(request,'lista_videojuegos.html',{'Videojuegos_Mostrar':videojuegos})

#------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------

# Errores
def mi_error_404(request,exception=None):
    return render(request,'error/404.html',None,None,404)

def mi_error_403(request,exception=None):
    return render(request,'error/403.html',None,None,403)

def mi_error_400(request,exception=None):
    return render(request,'error/400.html',None,None,400)

def mi_error_500(request,exception=None):
    return render(request,'error/500.html',None,None,500)