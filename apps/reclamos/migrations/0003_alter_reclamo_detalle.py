# Generated by Django 3.2 on 2023-05-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamos', '0002_alter_reclamo_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamo',
            name='detalle',
            field=models.CharField(max_length=500, null=True, verbose_name='Detalles'),
        ),
    ]