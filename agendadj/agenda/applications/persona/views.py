from django.shortcuts import render
from django.views.generic import ListView

from rest_framework.generics import ListAPIView

from .models import Person

from .serializers import PersonsSerializer

class ListPersonaListView(ListView):
    template_name = "persona/personas.html"
    context_object_name = "personas"

    def get_queryset(self):
        return Person.objects.all()

class PersonListAPIView(ListAPIView):
    serializer_class = PersonsSerializer

    def get_queryset(self):
        return Person.objects.all()

