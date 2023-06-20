# Generated by Django 3.2.14 on 2023-06-20 14:03

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
            name='Arbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urgencia', models.CharField(choices=[('', ''), ('1', 'Baja'), ('2', 'Media'), ('3', 'Alta')], default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Árbol',
                'verbose_name_plural': 'Árboles',
            },
        ),
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_vulgar', models.CharField(default='', max_length=50, verbose_name='Nombre_vulgar')),
                ('nombre_cientifico', models.CharField(default='', max_length=50, verbose_name='Nombre_cientifico')),
                ('nombre_completo', models.CharField(default='', max_length=50, verbose_name='Nombre_completo')),
            ],
        ),
        migrations.CreateModel(
            name='Inspeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inspeccion', models.DateField(verbose_name='Fecha de inspección')),
                ('reclamo', models.CharField(choices=[('', ''), ('1', 'Árbol caído'), ('2', 'Árbol con riesgo de caída'), ('3', 'Árbol electrificado'), ('4', 'Corte de raíz'), ('5', 'Despeje de cables'), ('6', 'Despeje luminario'), ('7', 'Extracción'), ('8', 'Indemnización'), ('9', 'Panal de abejas/avispas'), ('10', 'Poda'), ('11', 'Poda sin autorización'), ('12', 'Queja'), ('13', 'Rama quebrada'), ('14', 'Recolección de poda'), ('15', 'Revisión de estado del árbol'), ('16', 'Solicitud de árbol'), ('17', 'Solicitud de autorización'), ('18', 'Tala sin autorización')], default='', max_length=100, verbose_name='Reclamo inspección')),
                ('inspector', models.CharField(choices=[('', ''), ('1', 'Pepe Guardiola'), ('2', 'Miguel conejito Alejandro'), ('3', 'Angela Merkel')], default='', max_length=100, verbose_name='Inspector designado')),
                ('lugar', models.CharField(choices=[('', ''), ('1', 'Zona Este'), ('2', 'Zona Oeste'), ('3', 'Zona Norte'), ('4', 'Zona Sur')], default='', max_length=100, verbose_name='Lugar geográfico de la inspección')),
                ('nota', models.CharField(blank=True, max_length=300, verbose_name='Nota (opcional)')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img_inspeccion')),
                ('especie', models.CharField(choices=[('', ''), ('1', 'Jacarandá'), ('2', 'Ceibo'), ('3', 'Lapacho')], default='', max_length=100, verbose_name='Especie')),
                ('trabajo', models.CharField(choices=[('', ''), ('PI', 'Poda Integral'), ('PR', 'Poda Reductiva'), ('PD', 'Poda de Despeje'), ('T', 'Tala'), ('CR', 'Corte de Raíces'), ('E', 'Extracción')], default='', max_length=100)),
            ],
            options={
                'verbose_name': 'Inspeccion',
                'verbose_name_plural': 'Inspecciones',
                'db_table': 'inspeccion',
                'ordering': ['fecha_inspeccion', 'lugar', 'reclamo'],
            },
        ),
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
                ('disposicion', models.CharField(choices=[('BLANK ', ''), ('PUNTUAL', 'Puntual'), ('LINEAL', 'Lineal')], default='', max_length=20, verbose_name='Disposicion')),
                ('especie_altura', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Especie_altura')),
                ('dap', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Dap')),
                ('cableado_cercano', models.CharField(default='', max_length=50, null=True, verbose_name='Cableado_cercano')),
                ('construccion_cercana', models.CharField(max_length=50, null=True, verbose_name='Construccion_cercana')),
                ('observaciones_sitio', models.CharField(default='', max_length=50, null=True, verbose_name='Observaciones')),
                ('urgencia_trabajo', models.CharField(choices=[('', ''), ('1', 'Baja'), ('2', 'Media'), ('3', 'Alta')], default='', max_length=5, verbose_name='Urgencia')),
                ('justificacion', models.CharField(max_length=50, verbose_name='Justificacion')),
                ('fecha_carga_inspeccion', models.DateField(verbose_name='Fecha_carga_inspeccion')),
                ('codigo_trabajo', models.CharField(max_length=50, verbose_name='Codigo_trabajo')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img_reclamos', verbose_name='Fotos')),
                ('eliminado', models.BooleanField(default=False)),
                ('arbol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspeccion.arbol', verbose_name='arbol')),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspeccion.especies', verbose_name='Especie')),
                ('inspector', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario', verbose_name='inspector')),
                ('reclamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reclamos.reclamomodel', verbose_name='Reclamo')),
                ('trabajo_a_realizar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inspeccion.trabajos', verbose_name='trabajos')),
            ],
        ),
        migrations.AddField(
            model_name='arbol',
            name='inspeccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inspeccion.inspeccion'),
        ),
    ]
