# Generated by Django 5.0.6 on 2024-07-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_noticia_fecha_publicacion_noticia_fecha_subida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.IntegerField(choices=[(1, 'Deportes'), (2, 'Musica'), (3, 'Chile'), (4, 'Mundo'), (5, 'Salud')]),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]