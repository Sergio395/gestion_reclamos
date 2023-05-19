# Generated by Django 3.2.14 on 2023-05-19 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArbolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('calle', models.CharField(max_length=50, verbose_name='Calle')),
                ('numeracion', models.IntegerField(verbose_name='Numeración')),
                ('entre_calle_1', models.CharField(max_length=50, verbose_name='Entre calle')),
                ('entre_calle_2', models.CharField(max_length=50, verbose_name='y calle')),
                ('edificio', models.CharField(max_length=50, verbose_name='Edificio')),
                ('departamento', models.CharField(max_length=50, verbose_name='Departamento')),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitud')),
                ('especie', models.CharField(max_length=30, verbose_name='Especie')),
                ('altura', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Altura')),
            ],
        ),
    ]
