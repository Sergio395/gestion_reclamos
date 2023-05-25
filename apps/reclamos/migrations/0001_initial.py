# Generated by Django 3.2.14 on 2023-05-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inspeccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denunciante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('celular', models.IntegerField(verbose_name='Celular')),
                ('telefono_fijo', models.IntegerField(verbose_name='Telefono fijo')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('medio', models.CharField(choices=[('', ''), ('06', 'Calle'), ('00', 'CAV'), ('01', 'Expediente'), ('07', 'Correo electrónico'), ('05', 'Nota'), ('03', 'Redes sociales'), ('04', 'Teléfono Oficina'), ('02', 'Ventanilla'), ('08', 'WAP')], default='', max_length=50, verbose_name='Medio')),
                ('fuente', models.CharField(choices=[('', ''), ('1', 'Arquitectura'), ('2', 'CAV'), ('3', 'Ceremonial'), ('4', 'COM'), ('5', 'Consejo Deliberante'), ('6', 'Consejo Escolar'), ('7', 'Cultura'), ('8', 'Defensa Civil'), ('9', 'Delegación 9 de Julio'), ('10', 'Delegación Canning'), ('11', 'Delegación El Jagüel'), ('12', 'Delegación Luis Guillón'), ('13', 'Delegación Malvinas'), ('14', 'Delegación Monte Grande Sur'), ('15', 'EDESUR S.A.'), ('16', 'Enlace Echeverría'), ('17', 'Entidades'), ('18', 'Espacios Verdes'), ('19', 'Gobierno'), ('20', 'Medio Ambiente'), ('21', 'Mesa de Entrada'), ('22', 'Obras Hídricas'), ('23', 'Obras Particulares'), ('24', 'Obras Públicas'), ('25', 'Prensa'), ('26', 'Seguridad'), ('27', 'Servicios'), ('28', 'Vecino')], default='', max_length=50, verbose_name='Fuente')),
                ('fecha', models.DateField(verbose_name='Fecha del reclamo')),
                ('calle', models.CharField(max_length=50, verbose_name='Calle')),
                ('numeracion', models.IntegerField(verbose_name='Numeración')),
                ('edificio', models.CharField(max_length=50, verbose_name='Edificio')),
                ('departamento', models.CharField(max_length=50, verbose_name='Departamento')),
                ('entre_calle_1', models.CharField(max_length=50, verbose_name='Entre calle')),
                ('entre_calle_2', models.CharField(max_length=50, verbose_name='y calle')),
                ('localidad', models.CharField(choices=[('', ''), ('1', '9 de Abril'), ('2', 'Canning'), ('3', 'El Jagüel'), ('4', 'Luis Guillón'), ('5', 'Monte Grande')], default='', max_length=50, verbose_name='Localidad')),
                ('reclamo', models.CharField(choices=[('', ''), ('1', 'Árbol caído'), ('2', 'Árbol con riesgo de caída'), ('3', 'Árbol electrificado'), ('4', 'Corte de raíz'), ('5', 'Despeje de cables'), ('6', 'Despeje luminario'), ('7', 'Extracción'), ('8', 'Indemnización'), ('9', 'Panal de abejas/avispas'), ('10', 'Poda'), ('11', 'Poda sin autorización'), ('12', 'Queja'), ('13', 'Rama quebrada'), ('14', 'Recolección de poda'), ('15', 'Revisión de estado del árbol'), ('16', 'Solicitud de árbol'), ('17', 'Solicitud de autorización'), ('18', 'Tala sin autorización')], default='', max_length=200, verbose_name='Reclamo')),
                ('urgencia', models.CharField(choices=[('', ''), ('1', 'Baja'), ('2', 'Media'), ('3', 'Alta')], default='', max_length=5, verbose_name='Urgencia')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img_reclamos', verbose_name='Fotos')),
                ('detalle', models.CharField(max_length=500, verbose_name='Detalles')),
                ('arboles', models.ManyToManyField(to='inspeccion.Arbol', verbose_name='Arbol')),
                ('denunciantes', models.ManyToManyField(to='reclamos.Denunciante', verbose_name='Denunciante')),
            ],
        ),
    ]
