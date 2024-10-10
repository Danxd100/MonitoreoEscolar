from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registro.html', registro, name='registro'),
    path('registroadmin.html', registroadmin, name='registroadmin'),


    path('cursos/', views.listar_cursos, name='listar_cursos'),  # Ruta para listar cursos
    path('cursos/create/', views.crear_curso, name='crear_curso'),  # Ruta para crear curso
    path('cursos/<str:id_curso>/edit/', views.editar_curso, name='curso_form'),  # Ruta para editar curso
    path('cursos/<str:id_curso>/delete/', views.confirmar_eliminar, name='confirmar_eliminar'),  # Ruta para eliminar curso


    path('asignaturas/', views.listar_asignaturas, name='listar_asignaturas'),  # Ruta para listar asignaturas
    path('asignaturas/create/', views.crear_asignatura, name='crear_asignatura'),  # Ruta para crear asignatura
    path('asignaturas/<str:id_asignatura>/edit/', views.editar_asignatura, name='asignatura_form'),  # Ruta para editar asignatura
    path('asignaturas/<str:id_asignatura>/delete/', views.confirmar_eliminar_asignatura, name='eliminar_asignatura'),

]
