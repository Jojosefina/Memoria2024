import datetime
import os
from django.contrib.auth import authenticate, login
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.template import Template, Context, loader
from .forms import FileForm, RegisterForm
from .models import Asignaturas, Documentos, Etiquetas, Profesores, Account


def home(request):
    # get all documents, invert the list and return the first 3
    documentos = Documentos.objects.all()
    documentos = documentos[::-1][:3]
    return render(request, 'home.html', {'documentos': documentos})


def misApuntes(request):
    return render(request, 'misApuntes.html')


def divide_by_chunks(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]


def busqueda(request):
    query = request.GET.get('search', '')  # Obtener la consulta de búsqueda
    # Buscar documentos cuyo título contenga la consulta (insensible a mayúsculas/minúsculas)
    resultados = Documentos.objects.filter(
        titulo__icontains=query)  # Ajusta el campo según tu caso
    # Divide los resultados en grupos de 3
    lista_resultados = list(divide_by_chunks(resultados, 3))
    return render(request, 'search.html', {'resultados': lista_resultados, 'query': query})


def get_asignatura_id(asignatura):
    try:
        return Asignaturas.objects.get(nombre=asignatura).id_asignatura
    except Asignaturas.DoesNotExist:
        return None


def asignaturas(request):
    asignaturas = Asignaturas.objects.all()
    lista_asignaturas = list(divide_by_chunks(asignaturas, 3))
    return render(request, 'asignaturas.html', {'lista_asignaturas': lista_asignaturas})


def apuntesAsignaturas(request, id_asignatura):
    asignatura = get_object_or_404(Asignaturas, id_asignatura=id_asignatura)
    documentos_lista = Documentos.objects.filter(id_asignaturas=id_asignatura)
    documentos_chunks = list(divide_by_chunks(documentos_lista, 3))
    return render(request, 'apuntesAsignaturas.html', {'asignatura': asignatura, 'documentos': documentos_chunks})


def download_document(request, id_documento):
    try:
        documento = Documentos.objects.get(id_documento=id_documento)
        if documento.archivo:
            documento.cantidad_descargas += 1
            documento.save()
            response = FileResponse(documento.archivo.file, as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{documento.archivo.name}"'
            return response
        else:
            return HttpResponse("No se encontró el archivo.", status=404)
    except Documentos.DoesNotExist:
        return HttpResponse("Documento no encontrado.", status=404)


def post(request, id):
    # Encuentra el documento por su ID
    documento = get_object_or_404(Documentos, id_documento=id)
    etiquetas = documento.etiquetas.all()
    # Renderiza la plantilla 'post.html' con el documento obtenido
    return render(request, 'post.html', {'documento': documento, 'etiquetas': etiquetas})


def obtener_profesores_por_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignaturas, id_asignatura=asignatura_id)
    profesores = Profesores.objects.filter(asignatura=asignatura)
    profesores_json = [{"id": p.id_profesor, "nombre": p.nombre,
                        "apellido": p.apellido} for p in profesores]
    return JsonResponse(profesores_json, safe=False)


def subida(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            documento_instance = form.save(commit=False)
            documento_instance.id_usuario = Account.objects.filter(
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
    form = FileForm()
    return render(request, 'upload.html', {'form': form})


def registro(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"Ya has iniciado sesión como {user.correo}.")
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            form.save()
            email = form.cleaned_data.get('correo').lower()
            password = form.cleaned_data.get('password1')
            account = authenticate(correo=email, password=password)
            login(request, account)
            destination = kwargs.get('next')
            if destination:
                return redirect(destination)
            return redirect('home')
        else:
            print("Formulario inválido")
            print(form.errors)
            context['form'] = form
    else:
        context['form'] = RegisterForm()
    return render(request, 'register.html', context)
