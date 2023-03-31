from django.urls import path
from . import views

app_name = 'volumen'

urlpatterns = [
    # ex: /volumen/
    path('', views.index, name = 'index'),
    path('calcular', views.calcular, name = 'calcular'),
]

