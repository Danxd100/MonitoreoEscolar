from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


from .models import Curso
from .forms import CursoForm


from django.shortcuts import render, get_object_or_404, redirect
from .models import Asignatura
from .forms import AsignaturaForm

# Verificar si el usuario es administrador
def es_administrador(user):
    if user.is_superuser or user.is_staff:
        return True
    return HttpResponseRedirect('/')  



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Verificamos si el usuario es admin y redirigimos a la página correspondiente
            if user.is_superuser or user.is_staff:
                return redirect('registroadmin.html')  # Redirige a la página de administrador
            else:
                return redirect('registro.html')  # Redirige a la página principal si no es admin
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    
    return render(request, 'login.html')



def registro(request):

    return render(request, 'registro.html')





@user_passes_test(es_administrador)  # Restringir acceso solo a administradores
@login_required  # Asegura que esté autenticado
def registroadmin(request):

    return render(request, 'registroadmin.html')






# Listar cursos
@user_passes_test(es_administrador)  # Restringir acceso solo a administradores
@login_required  # Asegura que esté autenticado
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})

# Crear curso
@user_passes_test(es_administrador)  # Restringir acceso solo a administradores
@login_required  # Asegura que esté autenticado
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', {'form': form})

# Editar curso
@user_passes_test(es_administrador)  # Restringir acceso solo a administradores
@login_required  # Asegura que esté autenticado
def editar_curso(request, id_curso):
    curso = get_object_or_404(Curso, id_curso=id_curso)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso_form.html', {'form': form})

# Confirmar eliminación de curso
@user_passes_test(es_administrador)  # Restringir acceso solo a administradores
@login_required  # Asegura que esté autenticado
def confirmar_eliminar(request, id_curso):
    curso = get_object_or_404(Curso, id_curso=id_curso)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'confirmar_eliminar.html', {'curso': curso})








# Listar asignaturas
def listar_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'listar_asignaturas.html', {'asignaturas': asignaturas})

# Crear asignatura
def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_asignaturas')
    else:
        form = AsignaturaForm()
    return render(request, 'asignatura_form.html', {'form': form})


# Editar asignatura
def editar_asignatura(request, id_asignatura):
    asignatura = get_object_or_404(Asignatura, id_asignatura=id_asignatura)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('listar_asignaturas')  # Asegúrate de que esta URL esté definida
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'asignatura_form.html', {'form': form})


# Confirmar eliminación de asignatura
def confirmar_eliminar_asignatura(request, id_asignatura):
    asignatura = get_object_or_404(Asignatura, id_asignatura=id_asignatura)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('listar_asignaturas')
    return render(request, 'confirmar_eliminar.html', {'asignatura': asignatura})