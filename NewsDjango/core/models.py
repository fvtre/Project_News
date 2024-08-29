from django.db import models
from django.utils import timezone

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
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='media/',null=True)

    def __str__(self):
        return self.titular
    
class InicioSesion(models.Model):
    usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario
    
class Usuarioreg(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    rut = models.CharField(max_length=12) 
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField() 
    correo = models.EmailField(max_length=100)  
    contraseña = models.CharField(max_length=100)  
    genero = [
        (1, 'Masculino'),
        (2, 'Femenino'),
        (3, 'Otro'),
    ]
    genero = models.IntegerField(choices=genero) 
    comuna = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)  

    def __str__(self):
        return self.nombre_usuario