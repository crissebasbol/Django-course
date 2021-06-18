from django.contrib import admin
from django.urls import path

from . import views

app_name = 'persona_app'

urlpatterns = [
    path('list_all_empleados/', views.ListAllEmpleados.as_view()),
    path('list_by_deparment/<name_department>', views.ListByDepartment.as_view()),
    path('list_by_job/<job>', views.ListByJob.as_view()),
    path('search_employer/', views.ListByKword.as_view()),
    path('list_habilities_employer/<id_employer>', views.ListHabilitiesEmployer.as_view()),
    path('see_employer/<pk>', views.EmployersDetailView.as_view()),
    path('add_employer', views.EmpleadoCreateView.as_view()),
    path(
        'success', 
        views.SuccessView.as_view(), 
        name='correct'
    ),
    path(
        'update_employer/<pk>', 
        views.EmployerUpdateView.as_view(), 
        name='update_emp'
    ),
    path(
        'delete_employer/<pk>', 
        views.EmployerDeleteView.as_view(), 
        name='delete_emp'
    ),
]
