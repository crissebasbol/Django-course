from django.contrib import admin
from .models import Empleado, Hability

# Register your models here.

admin.site.register(Hability)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job'
    )

admin.site.register(Empleado, EmpleadoAdmin)