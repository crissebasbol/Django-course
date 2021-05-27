from django.shortcuts import render
from django.views.generic import ListView, DetailView

#models
from .models import Empleado



class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = 'id'
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


class ListByJob(ListView):
    """ List employers by job"""
    template_name = "persona/list_by_job.html"

    def get_queryset(self):
        job = self.kwargs['job']
        list_employers = Empleado.objects.filter(
            job=job
        )
        return list_employers


class ListByKword(ListView):
    """ List employers by key workd """
    template_name = 'persona/by_kword.html'
    context_object_name = 'employers'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        list_employers = Empleado.objects.filter(
            first_name=kword
        )
        print(list_employers)
        return list_employers


class ListHabilitiesEmployer(ListView):
    template_name = 'persona/habilities.html'
    context_object_name = 'habilities'

    def get_queryset(self):
        id_employer = self.kwargs['id_employer']
        employer = Empleado.objects.get(id=id_employer)
        return employer.habilities.all()



class EmployersDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_employer.html"

    
    def get_context_data(self, **kwargs):
        context = super(EmployersDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Employee of the month'
        return context
    
