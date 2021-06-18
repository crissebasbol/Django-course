from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
)

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



class SuccessView(TemplateView):
    template_name = "persona/success.html"

    

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/create_employer.html"
    #fields = ['first_name', 'last_name', 'job']
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilities'
    ]
    success_url = reverse_lazy('persona_app:correct')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmployerUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilities'
    ]
    success_url = reverse_lazy('persona_app:correct')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmployerUpdateView, self).form_valid(form)


class EmployerDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correct')


