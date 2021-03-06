# Generated by Django 2.2.16 on 2020-10-31 06:01

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidad Empleados',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='Nombres completos')),
                ('job', models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO'), ('4', 'ENFERMERA'), ('5', 'INGENIERO')], max_length=1, verbose_name='Trabajo')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='empleado')),
                ('hoja_vida', ckeditor.fields.RichTextField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.Departamento')),
                ('habilidades', models.ManyToManyField(to='persona.Habilidades')),
            ],
            options={
                'verbose_name': 'Mi Personal',
                'verbose_name_plural': 'Area de Recursos Humanos',
                'ordering': ['last_name'],
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
