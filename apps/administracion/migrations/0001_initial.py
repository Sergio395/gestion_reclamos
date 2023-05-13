# Generated by Django 3.2 on 2023-05-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('usuario', models.CharField(max_length=15, verbose_name='Usuario')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('clave', models.CharField(max_length=20, verbose_name='Clave')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('usuario', models.CharField(max_length=15, verbose_name='Usuario')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('clave', models.CharField(max_length=20, verbose_name='Clave')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inspector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('usuario', models.CharField(max_length=15, verbose_name='Usuario')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('clave', models.CharField(max_length=20, verbose_name='Clave')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('usuario', models.CharField(max_length=15, verbose_name='Usuario')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('clave', models.CharField(max_length=20, verbose_name='Clave')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
