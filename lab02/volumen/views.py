
from django.shortcuts import render
import math

def index(request):
    context = {
        'titulo': "Calcular",
    }
    return render(request, 'volumen/formulario.html', context)

def calcular(request):
    diametro = float(request.POST.get('diametro'))
    altura = float(request.POST.get('altura'))

    # Validacion
    if not diametro or not altura:
        mensaje_error = "Por favor ingrese ambos números"
        return render(request, 'volumen/formulario.html', {'mensaje_error': mensaje_error})

    volumen = math.pi * (diametro / 2) ** 2 * altura
    context = {
        'titulo': "Resultado",
        'diametro': diametro,
        'altura': altura,
        'resultado': round(volumen,2)
    }
    return render(request, 'volumen/resultado.html', context)

