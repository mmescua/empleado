# Generated by Django 2.2.6 on 2020-09-09 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
