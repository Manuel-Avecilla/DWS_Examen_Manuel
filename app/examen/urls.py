from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('lista/videojuegos/<str:titulo>/<str:pais>',views.dame_videojuegos_titulo_pais, name='dame_videojuegos_titulo_pais'),
]