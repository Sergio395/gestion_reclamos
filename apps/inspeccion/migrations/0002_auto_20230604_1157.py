# Generated by Django 3.2 on 2023-06-04 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
        ('inspeccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspecciones',
            name='arbol',
            field=models.ForeignKey(blank='', null=True, on_delete=django.db.models.deletion.CASCADE, to='inspeccion.arbol', verbose_name='arbol'),
        ),
        migrations.AlterField(
            model_name='inspecciones',
            name='inspector',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario', verbose_name='inspector'),
        ),
    ]
