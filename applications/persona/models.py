from django.db import models
from ckeditor.fields import RichTextField
#
from applications.departamento.models import Departamento
# New Table added
class Habilidades(models.Model):
    habilidad= models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidad Empleados'

    def __str__(self):
        return  self.habilidad +' - '+str(self.id)

# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla Empleados"""
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
        ('4', 'ENFERMERA'),
        ('5', 'INGENIERO'),
    )
    #contador
    #Administrador
    #Economista
    #Otro
    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo',max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    #image = models.ImageField(,upload_to=None, height_field=None, width_field=None)
    #Added relation many to many
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Personal'
        verbose_name_plural = 'Area de Recursos Humanos'
        ordering = ['last_name'] #Ascending
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return  self.last_name +', '+ self.first_name+' '+'ID:'+str(self.id)