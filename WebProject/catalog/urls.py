from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('misApuntes/', views.misApuntes, name='misApuntes'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('asignaturas/', views.asignaturas, name='asignaturas'),
    path('apuntesAsignaturas/', views.apuntesAsignaturas,
         name='ApuntesAsignaturas'),
    path('post/<int:id>', views.post, name='Post'),
    path('upload/', views.subida, name='upload'),
    path('registro/', views.registro, name='Registro'),
]
