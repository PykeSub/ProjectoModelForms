from django.shortcuts import render
from formAPP.forms import formProyecto
from formAPP.models import Proyecto

# Create your views here.
def index(request):
    return render(request, 'formApp/index.html')

def listadoProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'formApp/proyectos.html', data)

def agregarProyecto(request):
    form = formProyecto()
    if request.method == 'POST':
        form = formProyecto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'formApp/agregarProyecto.html', data)

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return render('/proyectos')

def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    form = formProyecto(instance=proyecto)
    if request.method == 'POST':
        form = formProyecto(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'formApp/agregarProyecto.html', data)