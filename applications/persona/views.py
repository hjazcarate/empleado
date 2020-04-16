from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
) 
# models
from .models import Empleado
# forms
from .forms import EmpleadoForm

# Create your views here.
class InicioView(TemplateView):
    """ Vista que carga la pagina de inicion"""
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    # se asigna paginacion en bloques de 4 reg y se crea un objeto 'pag_obj'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    # model = Empleado  -> ya no se necesita el model
    def get_queryset(self):
        # print('************************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    # se asigna paginacion en bloques de 10 
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado  
    

class ListByAreaEmpleado(ListView):
    """ Lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    # queryset = Empleado.objects.filter(
    #     departamento__shor_name = 'Mantenimiento'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return lista


class ListByTrabajoEmpleado(ListView):
    """ Lista empleados de un area asigna argumento"""
    template_name = 'persona/list_by_trabajo.html'

    def get_queryset(self):
        area = self.kwargs['jobemp']
        lista = Empleado.objects.filter(
            job = area
        )
        return lista


class ListEmpleadosByKword(ListView):
    """ Lista de empleado por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('************************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)
        # Lista de la tabla empleado todas las habilidades
        return empleado.habilidades.all()

# 1. - Lista todos los empleados de la empresa
# 2. - Listar todos los empleados que pertenecen a un area de la empresa
# 3. - Listar empleados por trabajao
# 4. - Listar los empleados por palabras clave
# 5. - Listar habilidades de un empleado

class EmpleadoDetailView(DetailView):
    model = Empleado
    # <pk> hace referencia a un id interno
    template_name = 'persona/detail_empleado.html'

    # añadimos el get_context_data para añadir un texto al titulo definido en el template
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name =  'persona/success.html'


#class EmpleadoCreateView(CreateView):
#    model = Empleado
#    template_name = 'persona/add.html'
#    # fields = ('__all__') -> muestra todos los campos
#    fields = [
#        'first_name',
#        'last_name',
#        'job',
#        'departamento',
#        'avatar',
#        'habilidades',
#    ]
#    success_url = reverse_lazy('persona_app:empleado_admin')

# este form EmpleadoForm lo asiganamos a esta vista y reemplaza la anterior CreateView cambiamos la forma de pintar forms
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    form_class = EmpleadoForm 
    success_url = reverse_lazy('persona_app:empleado_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        # print(empleado) --> para comprobar en prompt que se graba el reg.
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('********METODO POST*********')
        print('***************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('********METODO form_valid *********')
        print('***************************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = 'persona/delete.html'
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')  


