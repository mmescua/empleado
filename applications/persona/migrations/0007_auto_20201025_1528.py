# Generated by Django 2.2.6 on 2020-10-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_empleado_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO'), ('4', 'ENFERMERA'), ('5', 'INGENIERO')], max_length=1, verbose_name='Trabajo'),
        ),
    ]