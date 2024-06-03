import datetime
import os
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.template import Template, Context, loader
from django.urls import reverse
from .forms import FileForm, RegisterForm, CommentForm, RateForm
from .models import Asignaturas, Comentarios, Documentos, Etiquetas, Profesores, Account, Semestres


def home(request):
    # get all documents, invert the list and return the first 3
    documentos = Documentos.objects.all()
    documentos = documentos[::-1][:3]
    return render(request, 'home.html', {'documentos': documentos})


def divide_by_chunks(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]


def misApuntes(request):
    user = request.user
    documentos_user = Documentos.objects.filter(id_usuario=user)
    favoritos = user.favoritos.all()
    lista_documentos = list(divide_by_chunks(documentos_user, 3))
    return render(request, 'misApuntes.html', {'favoritos': favoritos, 'documentos': lista_documentos})


def favoritos(request):
    favoritos = request.user.favoritos.all()
    lista_favoritos = list(divide_by_chunks(favoritos, 3))
    return render(request, 'favoritos.html', {'favoritos': lista_favoritos})


def agregar_favorito(request, id_documento):
    user = request.user
    documento = get_object_or_404(Documentos, id_documento=id_documento)
    if documento in user.favoritos.all():
        user.favoritos.remove(documento)
    else:
        user.favoritos.add(documento)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


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


def filtrar_asignaturas(request):
    semestre_id = request.GET.get('semestre')
    semestres = Semestres.objects.all()
    if semestre_id:
        asignaturas = Asignaturas.objects.filter(
            semestres__id_semestre=semestre_id)
    else:
        asignaturas = Asignaturas.objects.all()

    lista_asignaturas = list(divide_by_chunks(asignaturas, 3))
    context = {'lista_asignaturas': lista_asignaturas, 'semestres': semestres}
    return render(request, 'asignaturas.html', context)


def asignaturas(request):
    semestres = Semestres.objects.all()
    asignaturas = Asignaturas.objects.all()
    lista_asignaturas = list(divide_by_chunks(asignaturas, 3))
    return render(request, 'asignaturas.html', {'lista_asignaturas': lista_asignaturas, 'semestres': semestres})


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
    documento = get_object_or_404(Documentos, id_documento=id)
    etiquetas = documento.etiquetas.all()
    comentarios = Comentarios.objects.filter(id_documento_asociado=id)
    nuevo_comentario = None
    user = request.user
    fav = False
    if user.is_authenticated:
        fav = documento in user.favoritos.all()

    if request.method == 'POST':
        if 'contenido' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                nuevo_comentario = form.save(commit=False)
                nuevo_comentario.id_usuario = user
                nuevo_comentario.id_documento_asociado = documento
                nuevo_comentario.fecha = datetime.datetime.now()
                nuevo_comentario.save()
                return redirect(reverse('Post', kwargs={'id': documento.id_documento}))
        elif 'calificacion' in request.POST:
            form = RateForm(request.POST)
            if form.is_valid():
                nueva_calificacion = form.cleaned_data['calificacion']
                documento.calificaciones_usuarios[str(
                    user.id_usuario)] = nueva_calificacion
                documento.num_calificaciones = len(
                    documento.calificaciones_usuarios)
                total_calificaciones = sum(
                    map(int, documento.calificaciones_usuarios.values()))
                documento.calificacion = total_calificaciones / documento.num_calificaciones
                documento.save()
                return redirect(reverse('Post', kwargs={'id': documento.id_documento}))
    else:
        form = CommentForm()
        rate_form = RateForm()

    return render(request, 'post.html', {
        'documento': documento,
        'etiquetas': etiquetas,
        'comentarios': comentarios,
        'form': form,
        'rate_form': rate_form,
        'fav': fav,
    })


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


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        password = request.POST.get('password')
        user = authenticate(correo=email, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página de inicio después del inicio de sesión exitoso
            return redirect('home')
        else:
            # Aquí puedes manejar el caso en el que las credenciales son inválidas
            return HttpResponse('Credenciales inválidas', status=401)
    else:
        # Aquí puedes manejar el caso en el que no se haya enviado un formulario de inicio de sesión
        return HttpResponse('Método no permitido', status=405)


def logout_view(request):
    logout(request)
    return redirect('home')
