from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# import models
from .models import Prueba

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'arrayNumber'
    queryset = ['0', '10', '20', '30']


class ListPrueba(ListView):
    template_name = 'home/list_prueba.html'
    model = Prueba
    context_object_name = 'list'