from django.shortcuts import render

def index(request):
    context = {
        'titulo': "Calculadora",
    }
    return render(request, 'calculadora/formulario.html', context)

def calcular(request):
    num1 = request.POST.get('num1')
    num2 = request.POST.get('num2')
    opcion = request.POST.get('operacion')

    # Validaciones
    if not num1 or not num2:
        mensaje_error = "Por favor ingrese ambos números"
        return render(request, 'calculadora/formulario.html', {'mensaje_error': mensaje_error})

    num1 = int(num1)
    num2 = int(num2)
    if opcion == "suma":
        resultado = num1 + num2
        operacion = "suma"
        operador = '+'
    elif opcion == "resta":
        resultado = num1 - num2
        operacion = "resta"
        operador = '-'
    else:
        resultado = num1 * num2
        operacion = "multiplicación"
        operador = '*'

    context = {
        'titulo': "Resultado",
        'num1': num1,
        'num2': num2,
        'operacion': operacion,
        'operador': operador,
        'resultado': resultado
    }
    return render(request, 'calculadora/resultado.html', context)

