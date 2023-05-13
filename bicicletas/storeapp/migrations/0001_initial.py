# Generated by Django 4.2.1 on 2023-05-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre de la tienda')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Direccion de la tienda')),
                ('contact_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero de contacto')),
                ('phone', models.CharField(blank=True, max_length=14, null=True, verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Correo electronico')),
                ('website', models.URLField(blank=True, max_length=255, null=True, verbose_name='Sitio web')),
            ],
        ),
    ]