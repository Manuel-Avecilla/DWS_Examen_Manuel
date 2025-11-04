from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('lista/videojuegos/<str:titulo>/<str:pais>',views.dame_videojuegos_titulo_pais, name='dame_videojuegos_titulo_pais'),
    path('lista/videojuegos-buenos/<str:fabricante>/<str:nombre_plataforma>/<int:puntuacion>',views.dame_videojuegos_buenos, name='dame_videojuegos_buenos'),
    path('lista/videojuegos-sin-plataformas/',views.dame_videojuegos_sin_plataformas,name='dame_videojuegos_sin_plataformas'),
]