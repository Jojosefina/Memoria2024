from django.contrib import admin
from .models import TiposMaterial, Asignaturas, Profesores, Semestres, Comentarios, Etiquetas, Documentos, Usuarios
# Register your models here.


@admin.register(TiposMaterial)
class TiposMaterialAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_material', 'nombre')
    search_fields = ('nombre',)
    list_display_links = ('nombre',)


@admin.register(Asignaturas)
class AsignaturasAdmin(admin.ModelAdmin):
    list_display = ('id_asignatura', 'nombre', 'codigo_curso')
    search_fields = ('nombre', 'codigo_curso')
    list_display_links = ('id_asignatura', 'nombre', 'codigo_curso')


@admin.register(Profesores)
class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ('id_profesor', 'nombre', 'apellido')
    search_fields = ('nombre', 'apellido')
    list_display_links = ('id_profesor', 'nombre', 'apellido')


@admin.register(Semestres)
class SemestresAdmin(admin.ModelAdmin):
    list_display = ('id_semestre', 'nombre')
    search_fields = ('nombre',)
    list_display_links = ('id_semestre', 'nombre')


@admin.register(Comentarios)
class Comentarios(admin.ModelAdmin):
    list_display = ('id_comentario', 'id_documento_asociado',
                    'id_usuario', 'fecha', 'contenido')
    search_fields = ('id_documento_asociado',
                     'id_usuario', 'fecha', 'contenido')
    list_display_links = (
        'id_comentario', 'id_documento_asociado', 'id_usuario', 'fecha', 'contenido')


@admin.register(Etiquetas)
class EtiquetasAdmin(admin.ModelAdmin):
    list_display = ('id_etiqueta', 'nombre')
    search_fields = ('nombre',)
    list_display_links = ('id_etiqueta', 'nombre')


@admin.register(Documentos)
class DocumentosAdmin(admin.ModelAdmin):
    list_display = ('id_documento', 'titulo', 'id_usuario',
                    'fecha_subida', 'id_tipo_material', 'id_asignaturas', 'archivo', 'calificacion', 'cantidad_descargas')
    search_fields = ('titulo', 'id_usuario',
                     'fecha_subida', 'id_tipo_material', 'id_asignaturas', 'archivo', 'calificacion', 'cantidad_descargas')
    list_display_links = ('id_documento', 'titulo', 'id_usuario',
                          'fecha_subida', 'id_tipo_material', 'id_asignaturas', 'archivo', 'calificacion', 'cantidad_descargas')


@admin.register(Usuarios)
class Usuarios(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'apellido',
                    'correo', 'fecha_nacimiento', 'fecha_ingreso')
    search_fields = ('id_usuario', 'nombre', 'apellido',
                     'correo', 'fecha_nacimiento', 'fecha_ingreso')
    list_display_links = ('id_usuario', 'nombre', 'apellido',
                          'correo', 'fecha_nacimiento', 'fecha_ingreso')
