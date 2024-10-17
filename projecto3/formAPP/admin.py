from django.contrib import admin
from formAPP.models import Proyecto

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['fechaInicio', 'fechaTermino', 'nombre', 'responsable', 'prioridad']
# Register your models here.
admin.site.register(Proyecto)