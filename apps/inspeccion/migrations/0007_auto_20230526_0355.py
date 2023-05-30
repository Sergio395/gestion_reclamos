# Generated by Django 3.2 on 2023-05-26 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
        ('inspeccion', '0006_alter_inspecciones_especie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspecciones',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspeccion.especies', verbose_name='Especie'),
        ),
        migrations.RemoveField(
            model_name='inspecciones',
            name='inspector',
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='inspector',
            field=models.ManyToManyField(to='administracion.Usuario', verbose_name='inspector'),
        ),
    ]