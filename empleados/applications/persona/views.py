from django.shortcuts import render
from django.views.generic import ListView

#models
from .models import Empleado



class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    model = Empleado
