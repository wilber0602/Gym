from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from gymdb.models import Usuario


def login_view(request):
    if request.user.is_authenticated:
        if request.user.id_rol:
            if request.user.id_rol.nombre == "admin":
                return redirect('paneladmin')
            elif request.user.id_rol.nombre == "coach":
                return redirect('panelcoach')
            else:
                return redirect('panelUsuario')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.id_rol:
                if user.id_rol.nombre == "admin":
                    return redirect('paneladmin')
                elif user.id_rol.nombre == "coach":
                    return redirect('panelcoach')
                else:
                    return redirect('panelUsuario')
            else:
                return redirect('panelUsuario')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'login.html')


@login_required
def panel_coach(request):
    return render(request, 'coach/panelcoach.html', {'usuario': request.user})


@login_required
def panel_usuario(request):
    return render(request, 'usuario/panelusuario.html', {'usuario': request.user})
@login_required
def ver_progreso(request):
    return render(request, 'usurio/progreso.html')


@login_required
def panel_admin(request):
    return render(request, 'admin/paneladmin.html', {'usuario': request.user})

@login_required
def gestion_usuarios(request):
    return render(request, 'admin/gestionUsu.html')

@login_required
def gestion_Calorica(request):
    return render(request, 'admin/gestionCalorica.html')

@login_required
def reportes(request):
    return render(request, 'admin/reportes.html')

@login_required
def crear_rutinas(request):
    return render(request, 'admin/rutinas.html')

@login_required
def asignar_rutinas(request):
    return render(request, 'admin/asignarRutinas.html')

@login_required
def ver_progreso(request):
    return render(request, 'admin/progreso.html')

@login_required
def registrar_asistencia(request):
    return render(request, 'admin/asistencia.html')

@login_required
def finanzas(request):
    return render(request, 'admin/Finanzas.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
