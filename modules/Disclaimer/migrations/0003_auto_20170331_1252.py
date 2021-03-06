# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-31 18:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Disclaimer', '0002_auto_20170321_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volumetrico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volPre_recepcion', models.DateField(blank=True, null=True)),
                ('vol_po_solitada', models.DateField(blank=True, null=True)),
                ('vol_po_monto', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('vol_final_recibido', models.DateField(blank=True, null=True)),
                ('vol_final_vobo', models.CharField(blank=True, max_length=50, null=True)),
                ('vol_envio_att', models.DateField(blank=True, null=True)),
                ('vol_monto_venta', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('vol_valida_att', models.DateField(blank=True, null=True)),
                ('vol_creado', models.DateField(auto_now_add=True)),
            ],
            options={
                'permissions': (('contra_view', 'Contratista Can View'), ('mastec_view', 'Mastec Can View')),
            },
        ),
        migrations.AddField(
            model_name='levantamiento',
            name='ss_recibido',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='cuadrilla',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='ciudad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='coordinador_att',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='gerente_att',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='site_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='telefono_cellowner',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volumetrico',
            name='sitio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sitio_presupto', to='Disclaimer.Sitio'),
        ),
        migrations.AddField(
            model_name='volumetrico',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_presupto', to=settings.AUTH_USER_MODEL),
        ),
    ]
