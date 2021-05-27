from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('list_all_empleados/', views.ListAllEmpleados.as_view()),
]
