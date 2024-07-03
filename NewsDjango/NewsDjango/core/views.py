from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Inicio')  # Redirige a la página de inicio después del inicio de sesión exitoso
            else:
                messages.error(request, 'Contraseña incorrecta.')
        else:
            messages.error(request, 'El usuario no existe. Por favor, registra una cuenta.')

    return render(request, 'registration/Login.html')

def logout_view(request):
    logout(request)
    return redirect('Inicio')

def Inicio(request):
    noticias = Noticia.objects.all()
    context={
        'noticias': noticias
    }
    return render(request, 'core/Inicio.html', context)

def Chile(request):
    return render(request, 'core/Chile.html')
def Chileclausuranbarberia(request):
    return render(request, 'core/Chile-clausuran-barberia.html')
def Chileeducaciondigital(request):
    return render(request, 'core/Chile-educacion-digital.html')
def Chilesinviolencia(request):
    return render(request, 'core/Chile-sin-violencia.html')

def Contacto(request):
    return render(request, 'core/Contacto.html')

def Deportes(request):
    return render(request, 'core/Deportes.html')
def Deportespeleamike(request):
    return render(request, 'core/Deportes-pelea-mike.html')
def Deportescolocolo(request):
    return render(request, 'core/Deportes-colo-colo.html')
def DeportesNBA(request):
    return render(request, 'core/Deportes-NBA.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def Mundo(request):
    return render(request, 'core/Mundo.html')
def Mundomatanjorgemaldonado(request):
    return render(request, 'core/Mundo-matan-jorge-maldonado.html')
def Mundoisraelataca(request):
    return render(request, 'core/Mundo-israel-ataca.html')

def Musica(request):
    return render(request, 'core/Musica.html')
def Musicaaidiferencia(request):
    return render(request, 'core/Musica-ai-diferencia.html')
def Musicavicoc(request):
    return render(request, 'core/Musica-vico.c.html')
def Musicaaisabattlebeast(request):
    return render(request, 'core/Musica-aisa-battle-beast.html')
def Musicaironmaidenenchile2024(request):
    return render(request, 'core/Musica-iron-maiden-en-chile-2024.html')

@login_required
def nuevanoticia(request):
    return render(request, 'core/nuevanoticia.html')

def Salud(request):
    return render(request, 'core/Salud.html')
def Saluddengue(request):
    return render(request, 'core/Salud-dengue.html')
def Saludnanotecnologia(request):
    return render(request, 'core/Salud-nanotecnologia.html')
def Saludporelderecho(request):
    return render(request, 'core/Salud-por-el-derecho.html')


def formulario(request):
    return render(request, 'core/formulario.html')

