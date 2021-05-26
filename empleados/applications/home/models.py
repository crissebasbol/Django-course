from django.db import models

# Create your models here.

class Prueba(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title + ', ' + self.subtitle 