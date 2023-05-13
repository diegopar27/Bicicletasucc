# Generated by Django 4.2.1 on 2023-05-13 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('price', models.CharField(blank=True, max_length=10, null=True, verbose_name='Precio')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='Modelo')),
                ('types', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tipo')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categoryapp.category', verbose_name='Categoria')),
            ],
        ),
    ]