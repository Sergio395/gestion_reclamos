# Generated by Django 3.2 on 2023-05-26 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
        ('inspeccion', '0009_alter_inspecciones_reclamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspecciones',
            name='inspector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inspeccion', to='administracion.usuario', verbose_name='inspector'),
        ),
    ]
