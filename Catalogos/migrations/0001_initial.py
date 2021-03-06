# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CicloEscolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=20)),
                ('id_ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogos.CicloEscolar')),
                ('id_escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogos.Escuela')),
                ('id_grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogos.Grado')),
            ],
        ),
        migrations.CreateModel(
            name='NivelEducativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=25)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogos.Escuela')),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='id_nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogos.NivelEducativo'),
        ),
    ]
