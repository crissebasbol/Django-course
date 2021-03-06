from django.contrib import admin
from .models import Empleado, Hability

# Register your models here.

admin.site.register(Hability)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields = (
        'first_name',
    )

    list_filter = (
        'job',
        'habilities',
        'departamento',
    )

    filter_horizontal = (
        'habilities',
    )

admin.site.register(Empleado, EmpleadoAdmin)