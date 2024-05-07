import os
import random
from django.db import models


class TiposMaterial(models.Model):
    id_tipo_material = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Tipo de Material'
        verbose_name_plural = 'Tipos de Material'

    def __str__(self):
        return self.nombre


class Asignaturas(models.Model):
    id_asignatura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    codigo_curso = models.CharField(max_length=7)

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    def __str__(self):
        return self.nombre


class Profesores(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    asignatura = models.ManyToManyField(Asignaturas)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Semestres(models.Model):
    id_semestre = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    asignatura = models.ManyToManyField(Asignaturas)

    class Meta:
        verbose_name = 'Semestre'
        verbose_name_plural = 'Semestres'

    def __str__(self):
        return self.nombre


class Etiquetas(models.Model):
    id_etiqueta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.nombre


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre + ' ' + self.apellido


def change_file_name(instance, filename):
    path = 'pdf/'
    random_number = random.randint(1000, 9999)
    fileName = f"{random_number}.{filename.split('.')[-1]}"
    return os.path.join(path, fileName)


class Documentos(models.Model):
    id_documento = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    id_usuario = models.ForeignKey(
        Usuarios, on_delete=models.SET_NULL, null=True)
    fecha_subida = models.DateField()
    id_tipo_material = models.ForeignKey(
        TiposMaterial, on_delete=models.SET_NULL, null=True)
    id_asignaturas = models.ForeignKey(
        Asignaturas, on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey(
        Profesores, on_delete=models.SET_NULL, null=True)
    archivo = models.FileField(upload_to=change_file_name)
    calificacion = models.FloatField()
    cantidad_descargas = models.IntegerField()
    etiquetas = models.ManyToManyField(Etiquetas)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_documento_asociado = models.ForeignKey(
        Documentos, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField()
    contenido = models.TextField()

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
