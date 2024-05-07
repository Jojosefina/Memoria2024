import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.template import Template, Context, loader
from .forms import FileForm
from .models import Documentos, Etiquetas, Usuarios


def home(request):
    # get all documents, invert the list and return the first 3
    documentos = Documentos.objects.all()
    documentos = documentos[::-1][:3]
    return render(request, 'home.html', {'documentos': documentos})


def misApuntes(request):
    return render(request, 'misApuntes.html')


def busqueda(request):
    query = request.GET.get('search', '')  # Obtener la consulta de búsqueda
    # Buscar documentos cuyo título contenga la consulta (insensible a mayúsculas/minúsculas)
    resultados = Documentos.objects.filter(
        titulo__icontains=query)  # Ajusta el campo según tu caso

    return render(request, 'search.html', {'resultados': resultados, 'query': query})


def asignaturas(request):
    return render(request, 'asignaturas.html')


def apuntesAsignaturas(request):
    return render(request, 'apuntesAsignaturas.html')


def post(request, id):
    # Encuentra el documento por su ID
    documento = get_object_or_404(Documentos, id_documento=id)
    # Renderiza la plantilla 'post.html' con el documento obtenido
    return render(request, 'post.html', {'documento': documento})


def subida(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            documento_instance = form.save(commit=False)
            documento_instance.id_usuario = Usuarios.objects.filter(
                id_usuario=1).first()  # request.user
            documento_instance.fecha_subida = datetime.datetime.now()
            documento_instance.calificacion = 0
            documento_instance.cantidad_descargas = 0
            documento_instance.save()
            form.save_m2m()
            # redirect to post.html
            return redirect('Post', id=documento_instance.id_documento)
        else:
            return render(request, 'upload.html', {'form': form})
    form = FileForm(initial={'id_asignaturas': 0})
    return render(request, 'upload.html', {'form': form})


def registro(request):
    return render(request, 'register.html')
