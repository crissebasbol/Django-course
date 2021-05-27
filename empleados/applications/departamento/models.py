from django.db import models

# Create your models here.


class Departamento(models.Model):
    name = models.CharField('Name', max_length=50, blank=True, null=True)
    short_name = models.CharField('Short name', max_length=20, unique=True)
    anulate = models.BooleanField('Anulate', default=False)

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name', '-short_name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return str(self.id) + ', ' + self.name + ', '+ self.short_name