from django.contrib import admin
from django.urls import path

from . import views

app_name = "departamento_app"

# prueba
# def DesdeApps(self):
#    print("-----------Desde la Apps Departamento-------------")
# urlpatterns = [
#    path('departamento', DesdeApps),
#]

urlpatterns = [
    path('departamento-lista/', 
        views.DepartamentoListView.as_view(), 
        name='departamento_list'
    ),
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='nuevo_departamento'),
]