from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('misApuntes/', views.misApuntes, name='misApuntes'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('asignaturas/', views.asignaturas, name='asignaturas'),
    path('apuntesAsignaturas/<int:id_asignatura>/', views.apuntesAsignaturas,
         name='ApuntesAsignaturas'),
    path('post/<int:id>', views.post, name='Post'),
    path('upload/', views.subida, name='upload'),
    path('registro/', views.registro, name='Registro'),
    path('obtener-profesores/<int:asignatura_id>/',
         views.obtener_profesores_por_asignatura, name='obtener_profesores_por_asignatura'),
    path('download/<int:id_documento>/',
         views.download_document, name='download_document'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
