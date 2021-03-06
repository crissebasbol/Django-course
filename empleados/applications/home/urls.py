from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('list_prueba/', views.ListPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
]
