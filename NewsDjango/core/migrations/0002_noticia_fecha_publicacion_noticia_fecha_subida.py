# Generated by Django 5.0.6 on 2024-06-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='fecha_publicacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='fecha_subida',
            field=models.DateField(blank=True, null=True),
        ),
    ]
