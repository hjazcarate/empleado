from django.contrib import admin

from .models import Empleado, Habilidades

# Register your models here.

# admin.site.register(Empleado) -> bloqueamos introd decorador
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    #
    def full_name(self, obj):
        # aqui va toda la operacion en la nueva columna
        print('first_name')
        return obj.first_name + ' ' + obj.last_name
    #
    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades')

    # filtro ManyToMany
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)