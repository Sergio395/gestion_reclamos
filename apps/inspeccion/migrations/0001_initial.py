# Generated by Django 3.2 on 2023-05-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
        ('reclamos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_poda', models.CharField(max_length=50, verbose_name='Tipo_poda')),
                ('ubicacion', models.CharField(max_length=50, verbose_name='Ubicacion')),
                ('tipo_arbol', models.CharField(max_length=50, verbose_name='Tipo_arbol')),
                ('codigo', models.CharField(max_length=50, verbose_name='Codigo')),
                ('coeficiente', models.CharField(max_length=50, verbose_name='Coeficiente')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='inspecciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_requiere_inspeccion', models.BooleanField(default=False)),
                ('fecha_de_inspeccion', models.DateField(verbose_name='Fecha de inspeccion')),
                ('especie_altura', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Especie_altura')),
                ('dap', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Dap')),
                ('cableado_cercano', models.CharField(default='', max_length=50, verbose_name='Cableado_cercano')),
                ('construccion_cercana', models.CharField(max_length=50, verbose_name='Construccion_cercana')),
                ('observaciones_sitio', models.CharField(default='', max_length=50, verbose_name='Observaciones')),
                ('urgencia_trabajo', models.CharField(choices=[('', ''), ('1', 'Baja'), ('2', 'Media'), ('3', 'Alta')], default='', max_length=5, verbose_name='Urgencia')),
                ('justificacion', models.CharField(max_length=50, verbose_name='Justificacion')),
                ('fecha_carga_inspeccion', models.DateField(verbose_name='Fecha_carga_inspeccion')),
                ('codigo_trabajo', models.CharField(max_length=50, verbose_name='Codigo_trabajo')),
                ('eliminado', models.BooleanField(default=False)),
                ('arbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclamos.arbol', verbose_name='arbol')),
                ('inspector', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario', verbose_name='inspector')),
                ('reclamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclamos.reclamo', verbose_name='Reclamo')),
                ('trabajo_a_realizar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspeccion.trabajos', verbose_name='trabajos')),
            ],
        ),
    ]
