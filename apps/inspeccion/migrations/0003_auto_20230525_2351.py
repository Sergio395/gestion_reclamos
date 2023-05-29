# Generated by Django 3.2 on 2023-05-26 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
        ('reclamos', '0001_initial'),
        ('inspeccion', '0002_auto_20230525_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspecciones',
            name='arbol',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='reclamos.arbol', verbose_name='arbol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='cableado_cercano',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Cableado_cercano'),
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='codigo_trabajo',
            field=models.CharField(default='', max_length=50, verbose_name='Codigo_trabajo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='construccion_cercana',
            field=models.CharField(max_length=50, null=True, verbose_name='Construccion_cercana'),
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='fecha_carga_inspeccion',
            field=models.DateField(default="2000-01-01", verbose_name='Fecha_carga_inspeccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='inspector',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario', verbose_name='inspector'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='justificacion',
            field=models.CharField(default='', max_length=50, verbose_name='Justificacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='observaciones_sitio',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Observaciones'),
        ),
        migrations.AddField(
            model_name='inspecciones',
            name='urgencia_trabajo',
            field=models.CharField(choices=[('', ''), ('1', 'Baja'), ('2', 'Media'), ('3', 'Alta')], default='', max_length=5, verbose_name='Urgencia'),
        ),
        migrations.AlterField(
            model_name='inspecciones',
            name='disposicion',
            field=models.CharField(choices=[('BLANK ', ''), ('PUNTUAL', 'Puntual'), ('LINEAL', 'Lineal')], default='', max_length=20, verbose_name='Disposicion'),
        ),
    ]
