from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

def index(request):
    return render(request, 'index.html')

def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listar_laboratorios.html', {'laboratorios': laboratorios})

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'crear_laboratorio.html', {'form': form})

def detalle_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
    return render(request, 'detalle_laboratorio.html', {'laboratorio': laboratorio})

def actualizar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('listar_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'actualizar_laboratorio.html', {'form': form})

def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
    laboratorio.delete()
    return redirect('listar_laboratorios')