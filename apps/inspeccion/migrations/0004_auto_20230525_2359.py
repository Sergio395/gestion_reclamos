# Generated by Django 3.2 on 2023-05-26 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reclamos', '0001_initial'),
        ('inspeccion', '0003_auto_20230525_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspecciones',
            name='arbol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reclamos.arbol', verbose_name='arbol'),
        ),
        migrations.AlterField(
            model_name='inspecciones',
            name='reclamo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reclamos.reclamo', verbose_name='Reclamo'),
        ),
        migrations.AlterField(
            model_name='inspecciones',
            name='trabajo_a_realizar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspeccion.trabajos', verbose_name='trabajos'),
        ),
    ]