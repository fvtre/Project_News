# Generated by Django 5.0.6 on 2024-07-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_noticia_fecha_subida_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('genero', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino'), (3, 'Otro')], default=1)),
                ('comuna', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]