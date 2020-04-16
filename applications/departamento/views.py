from django.shortcuts import render
# importamos
from django.views.generic.edit import FormView
from applications.persona.models import Empleado 
from .models import Departamento
from django.views.generic import ListView

# no necesitamos especificar un modelo pero el form si necesita sobreescribir la funcion form_valid

from .forms import NewDepartamentoForm

class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = "departamentos"
    


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self,form):
        print('*********estamos en el form_valid **********')

        # Guardamos departamento
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()

        # Guardamos empleado
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )

        return super(NewDepartamentoView, self).form_valid(form)

