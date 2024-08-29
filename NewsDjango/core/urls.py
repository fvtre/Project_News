from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Login', Login, name='Login'),
    path('logout/', logout_view, name='logout'),
    path('', Inicio, name ='Inicio'),

    path('Deportes', Deportes, name='Deportes'),
    path('Deportes-pelea-mike', Deportespeleamike, name='Deportes-pelea-mike'),
    path('Deportes-colo-colo', Deportescolocolo, name='Deportes-colo-colo'),
    path('Deportes-NBA', DeportesNBA, name='Deportes-NBA'),

    path('Musica', Musica, name='Musica'),
    path('Musica-ai-diferencia', Musicaaidiferencia, name='Musica-ai-diferencia'),
    path('Musica-vico.c', Musicavicoc, name='Musica-vico.c'),
    path('Musica-aisa-battle-beast', Musicaaisabattlebeast, name='Musica-aisa-battle-beast'),
    path('Musica-iron-maiden-en-chile-2024', Musicaironmaidenenchile2024, name='Musica-iron-maiden-en-chile-2024'),

    path('Chile', Chile, name='Chile'),
    path('Chile-clausuran-barberia', Chileclausuranbarberia, name='Chile-clausuran-barberia'),
    path('Chile-educacion-digital', Chileeducaciondigital, name='Chile-educacion-digital'),
    path('Chile-sin-violencia', Chilesinviolencia, name='Chile-sin-violencia'),

    path('Mundo', Mundo, name='Mundo'),
    path('Mundo-matan-jorge-maldonado', Mundomatanjorgemaldonado, name='Mundo-matan-jorge-maldonado'),
    path('Mundo-israel-ataca', Mundoisraelataca, name='Mundo-israel-ataca'),

    path('Salud', Salud, name='Salud'),
    path('Salud-dengue', Saluddengue, name='Salud-dengue'),
    path('Salud-nanotecnologia', Saludnanotecnologia, name='Salud-nanotecnologia'),
    path('Salud-por-el-derecho', Saludporelderecho, name='Salud-por-el-derecho'),

    path('Contacto', Contacto, name='Contacto'),

    path('nuevanoticia', nuevanoticia, name='nuevanoticia'),

    path('formulario', formulario, name='formulario'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)