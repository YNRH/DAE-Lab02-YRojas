from django.shortcuts import render

def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST.get('nombre'),
        'clave': request.POST.get('password'),
        'educacion': request.POST.get('educacion'),
        'nacionalidad': request.POST.get('nacionalidad'),
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST.get('email'),
        'website': request.POST.get('sitioweb'),
    }
    return render(request, 'encuesta/respuesta.html', context)
