# region Explicación de los imports.
# ------------------------------------------------------------
# BaseCommand: permite crear comandos personalizados de Django.
# Faker: genera datos falsos (en español si se usa Faker('es_ES')).
# random: funciones aleatorias (choice, sample, randint...).
# Decimal: maneja decimales con precisión (para puntuaciones).
# timedelta: suma/resta días a fechas.
# timezone: obtiene fecha/hora actual con soporte de zona horaria.
# Modelos: importamos las clases necesarias del app examen.
# ------------------------------------------------------------
# endregion

# python manage.py generar_datos   <-- Comando para generar los datos

# python manage.py dumpdata --indent 4 > examen/fixtures/datos.json   <-- Comando para guardar los datos

from django.core.management.base import BaseCommand
from faker import Faker
import random
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from examen.models import *

class Command(BaseCommand):
    help = 'Generando datos usando Faker'

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')  # Faker en español
        
        self.stdout.write(self.style.SUCCESS("Datos generados correctamente."))