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
    search_fields = (
        'first_name',
    )
    list_filter = (
        'job',
        'habilities',
    )
    filter_horizontal = (
        'habilities',
    )

admin.site.register(Empleado, EmpleadoAdmin)