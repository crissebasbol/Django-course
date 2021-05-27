from django.db import models
from applications.departamento.models import Departamento
# Create your models here.

class Empleado(models.Model):
    """ Model for each employer """

    JOB_CHOICES = (
        ('0', 'Management'),
        ('1', 'Engineer'),
        ('2', 'Developer'),
    )

    first_name = models.CharField('First name', max_length=60)
    last_name = models.CharField('Last name', max_length=60)
    job = models.CharField('Job', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField('Imagen', upload_to=None, height_field=None, width_field=None, max_length=None)


    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['first_name', '-job']
        unique_together = ('first_name', 'job')


    def __str__(self):
        return str(self.id) + ', ' + self.first_name + ', ' + self.last_name

