# Generated by Django 5.0.6 on 2024-07-07 00:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_iniciosesion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='fecha_subida',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]