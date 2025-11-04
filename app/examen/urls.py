from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('lista/videojuegos/<str:titulo>/<str:pais>',views.dame_videojuegos_titulo_pais, name='dame_videojuegos_titulo_pais'),
    path('lista/videojuegos-buenos/<str:fabricante>/<str:nombre_plataforma>/<int:puntuacion>',views.dame_videojuegos_buenos, name='dame_videojuegos_buenos'),
    path('lista/videojuegos-sin-plataformas/',views.dame_videojuegos_sin_plataformas,name='dame_videojuegos_sin_plataformas'),
    path('lista/estudios-analisis/<int:year>',views.dame_estudios_analisis_year, name='dame_estudios_analisis_year'),
    path('lista/videojuegos/<int:id_estudio>/',views.dame_videojuegos_estudio_buenos, name='dame_videojuegos_estudio_buenos'),
    path('ultimo-analisis/<str:critico_nombre>/<str:fabricante>/<int:id_estudio>/<int:id_sede>',views.dame_ultimo_analisis, name='dame_ultimo_analisis'),
]