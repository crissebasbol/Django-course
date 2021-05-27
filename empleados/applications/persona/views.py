from django.shortcuts import render
from django.views.generic import ListView

#models
from .models import Empleado



class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    model = Empleado


class ListByDepartment(ListView):
    """ List employers by department"""
    template_name = "persona/list_by_deparment.html"

    def get_queryset(self):
        department = self.kwargs['name_department']
        list_employers = Empleado.objects.filter(
            departamento__name=department
        )
        return list_employers
