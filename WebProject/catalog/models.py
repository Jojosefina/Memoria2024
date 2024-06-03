import os
import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import JSONField


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


class UserManager(BaseUserManager):
    def create_user(self, correo, nombre, apellido, fecha_nacimiento, fecha_ingreso, password=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')
        if not nombre:
            raise ValueError('El usuario debe tener un nombre')
        if not apellido:
            raise ValueError('El usuario debe tener un apellido')
        if not fecha_nacimiento:
            raise ValueError('El usuario debe tener una fecha de nacimiento')
        if not fecha_ingreso:
            raise ValueError(
                'El usuario debe tener una fecha de ingreso a la universidad')

        user = self.model(
            correo=self.normalize_email(correo),
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            fecha_ingreso=fecha_ingreso
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombre, apellido, fecha_nacimiento, fecha_ingreso, password):
        user = self.create_user(
            correo=correo,
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            fecha_ingreso=fecha_ingreso,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    favoritos = models.ManyToManyField('Documentos', null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido',
                       'fecha_nacimiento', 'fecha_ingreso']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


def change_file_name(instance, filename):
    path = 'pdf/'
    random_number = random.randint(1000, 9999)
    fileName = f"{random_number}.{filename.split('.')[-1]}"
    return os.path.join(path, fileName)


class Documentos(models.Model):
    id_documento = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    id_usuario = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True)
    fecha_subida = models.DateField()
    id_tipo_material = models.ForeignKey(
        TiposMaterial, on_delete=models.SET_NULL, null=True)
    id_asignaturas = models.ForeignKey(
        Asignaturas, on_delete=models.SET_NULL, null=True)
    profesor = models.ForeignKey(
        Profesores, on_delete=models.SET_NULL, null=True)
    archivo = models.FileField(upload_to=change_file_name)
    calificacion = models.FloatField()
    num_calificaciones = models.IntegerField(default=0)
    cantidad_descargas = models.IntegerField()
    etiquetas = models.ManyToManyField(Etiquetas)
    calificaciones_usuarios = JSONField(default=dict)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'


class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_documento_asociado = models.ForeignKey(
        Documentos, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Account, on_delete=models.CASCADE)
    fecha = models.DateField()
    contenido = models.TextField()

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
