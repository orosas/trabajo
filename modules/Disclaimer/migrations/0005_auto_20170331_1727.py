# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-31 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disclaimer', '0004_auto_20170331_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='proveedor',
            field=models.CharField(blank=True, choices=[('DH', 'David Hernández'), ('ETL', 'ECOTEL'), ('FS', 'Franco & Soto'), ('FD', 'Freddy'), ('GICOM', 'Grupo ICOM'), ('GIP', 'Grupo IPE'), ('GVI', 'Grupo VALBRI'), ('GST', 'Grupo SET'), ('JAVCRUZ', 'Javier De La Cruz'), ('JAVJ', 'Javier Jiménez'), ('JJ', 'Juan Jesús'), ('MC', 'Macario Hernández'), ('MQ', 'Maqueda'), ('VK', 'Ve-Ca'), ('VI', 'Viadeza')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='proveedor',
            field=models.CharField(blank=True, choices=[('DH', 'David Hernández'), ('ETL', 'ECOTEL'), ('FS', 'Franco & Soto'), ('FD', 'Freddy'), ('GICOM', 'Grupo ICOM'), ('GIP', 'Grupo IPE'), ('GVI', 'Grupo VALBRI'), ('GST', 'Grupo SET'), ('JAVCRUZ', 'Javier De La Cruz'), ('JAVJ', 'Javier Jiménez'), ('JJ', 'Juan Jesús'), ('MC', 'Macario Hernández'), ('MQ', 'Maqueda'), ('VK', 'Ve-Ca'), ('VI', 'Viadeza')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='supervisor',
            field=models.CharField(blank=True, choices=[('OL', 'Oscar López'), ('PQ', 'Pablo Quezada'), ('FJ', 'Francisco Juárez'), ('MS', 'Miguel Salgado'), ('LG', 'Luis Gutierrez'), ('OM', 'Oscar Marín'), ('LD', 'Lino De La Rosa'), ('JP', 'Juan Pablo Flores'), ('ME', 'Martín Elías'), ('JG', 'Jaime García'), ('GJ', 'Gerardo Jiménez'), ('AB', 'Arturo Bautista'), ('AS', 'Antonio Salazar')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='volumetrico',
            name='vol_final_vobo',
            field=models.CharField(blank=True, choices=[('OL', 'Oscar López'), ('PQ', 'Pablo Quezada'), ('FJ', 'Francisco Juárez'), ('MS', 'Miguel Salgado'), ('LG', 'Luis Gutierrez'), ('OM', 'Oscar Marín'), ('LD', 'Lino De La Rosa'), ('JP', 'Juan Pablo Flores'), ('ME', 'Martín Elías'), ('JG', 'Jaime García'), ('GJ', 'Gerardo Jiménez'), ('AB', 'Arturo Bautista'), ('AS', 'Antonio Salazar')], max_length=50, null=True),
        ),
    ]
