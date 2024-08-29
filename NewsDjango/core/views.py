from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.
def get_weather_data(city):
    api_key = '22e4069d5f1ea10253646b46b1c1d5f3'  # Reemplaza esto con tu clave API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric&lang=es"
    response = requests.get(complete_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Retorna None si hay un problema con la solicitud

def get_news():
    api_key = 'd16c032d70714a34b67de63d630a90b2'  # Reemplaza esto con tu clave API de NewsAPI
    base_url = "https://newsapi.org/v2/top-headlines?"
    country = "co"  # Puedes cambiar esto por el país que desees
    complete_url = f"{base_url}country={country}&apiKey={api_key}"
    response = requests.get(complete_url)
    return response.json()

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
    noticias = Noticia.objects.order_by('-fecha_publicacion')
    news_data = get_news()
    city = "Puente Alto"
    weather_data = get_weather_data(city)

    context = {
        'noticias': noticias,
         'news_data': news_data,
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Inicio.html', context)

def Chile(request):
    news_data = get_news()
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
         'news_data': news_data,
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Chile.html', context)
    
def Chileclausuranbarberia(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Chile-clausuran-barberia.html', context)

def Chileeducaciondigital(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Chile-educacion-digital.html', context)
def Chilesinviolencia(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Chile-sin-violencia.html', context)

def Contacto(request):
    return render(request, 'core/Contacto.html')

def Deportes(request):
    news_data = get_news()
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
         'news_data': news_data,
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Deportes.html', context)
def Deportespeleamike(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Deportes-pelea-mike.html', context)
def Deportescolocolo(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Deportes-colo-colo.html', context)
def DeportesNBA(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Deportes-NBA.html', context)

def formulario(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)

    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/formulario.html' , context)

def Mundo(request):
    news_data = get_news()
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
         'news_data': news_data,
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Mundo.html', context)
def Mundomatanjorgemaldonado(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Mundo-matan-jorge-maldonado.html', context)
def Mundoisraelataca(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Mundo-israel-ataca.html', context)

def Musica(request):
    news_data = get_news()
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
         'news_data': news_data,
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Musica.html', context)
def Musicaaidiferencia(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Musica-ai-diferencia.html', context)
def Musicavicoc(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Musica-vico.c.html', context)
def Musicaaisabattlebeast(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Musica-aisa-battle-beast.html', context)
def Musicaironmaidenenchile2024(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Musica-iron-maiden-en-chile-2024.html', context)

@login_required
def nuevanoticia(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    if request.method == 'POST':
        nombre_periodista = request.POST.get('nombre_periodista')
        titular = request.POST.get('titular')
        categoria = request.POST.get('categoria')
        contenido_noticia = request.POST.get('contenido_noticia')
        
        imagen = request.FILES.get('imagen')  # Obtener la imagen desde request.FILES

        if not all([nombre_periodista, titular, categoria, contenido_noticia, imagen]):
            mensaje = "Todos los campos son obligatorios."
            context = {'mensaje': mensaje}
            return render(request, 'core/nuevanoticia.html', context)

        # Guarda la noticia en la base de datos
        noticia = Noticia.objects.create(
            nombre_periodista=nombre_periodista,
            titular=titular,
            categoria=categoria,
            contenido_noticia=contenido_noticia,
            imagen=imagen  # Asigna el archivo de imagen
            
        )
        noticia.save()

        mensaje = "Noticia publicada"
        context = {
            'mensaje': mensaje, 'weather_data': weather_data,
        'city': city,
        }
        return render(request, 'core/nuevanoticia.html', context)
    else:
        return render(request, 'core/nuevanoticia.html')

def Salud(request):
    news_data = get_news()
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
         'news_data': news_data,
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Salud.html', context)
def Saluddengue(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Salud-dengue.html', context)
def Saludnanotecnologia(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Salud-nanotecnologia.html', context)
def Saludporelderecho(request):
    city = "Puente Alto"
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'core/Salud-por-el-derecho.html', context)


def formulario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        rut = request.POST.get('rut')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        genero = int(request.POST.get('genero'))
        comuna = request.POST.get('comuna')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        # Crear instancia de Usuario y guardar en la base de datos
        usuario = Usuarioreg.objects.create(
            nombre_usuario=nombre_usuario,
            rut=rut,
            nombres=nombres,
            apellidos=apellidos,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            contraseña=contraseña,
            genero=genero,
            comuna=comuna,
            direccion=direccion,
            telefono=telefono
        )
        usuario.save()

        mensaje = "Nuevo usuario creado"
        context = {
            'mensaje': mensaje
        }
        return render(request, 'core/formulario.html', context)
    else:
        return render(request, 'core/formulario.html')

