from django.db import models

# Create your models here.
class  Noticia(models.Model):
    categoria = [
        (1, 'Deportes'),
        (2, 'Musica'),
        (3, 'Chile'),
        (4, 'Mundo'),
        (5, 'Salud'),
    ]
    nombre_periodista = models.CharField(max_length=100)
    titular = models.CharField(max_length=100)
    contenido_noticia = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=categoria)
    fecha_subida = models.DateField(null=True,blank=True)
    fecha_publicacion = models.DateField(null=True,blank=True)
    imagen = models.ImageField(upload_to='media/',null=True)

    def __str__(self):
        return self.titular
    
class InicioSesion(models.Model):
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario
    
