from django.shortcuts import render, redirect
from .models import Educacion, Experiencia, Habilidad, Proyecto
from app_1.forms import EducacionForm, ExperienciaForm, HabilidadForm, ProyectoForm, BuscarPersonaForm

def bienvenido(request):
    return render(request, "app_1/bienvenido.html")

def listar_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'app_1/listar_proyectos.html', {'proyectos': proyectos})

def nuevo_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'app_1/nuevo_proyecto.html', {'form': form})

def buscar_proyecto(request):
    form = BuscarPersonaForm()
    proyectos = []
    if request.method == 'GET':
        form = BuscarPersonaForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            proyectos = Proyecto.objects.filter(titulo__icontains=nombre)
    return render(request, 'app_1/buscar_proyectos.html', {'form': form, 'proyectos': proyectos})

def listar_habilidades(request):
    habilidades = Habilidad.objects.all()
    return render(request, 'app_1/listar_habilidades.html', {'habilidades': habilidades})

def nueva_habilidad(request):
    if request.method == 'POST':
        form = HabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_habilidades')
    else:
        form = HabilidadForm()
    return render(request, 'app_1/nueva_habilidad.html', {'form': form})

def listar_educacion(request):
    educaciones = Educacion.objects.all()
    return render(request, 'app_1/listar_educacion.html', {'educaciones': educaciones})

def nueva_educacion(request):
    if request.method == 'POST':
        form = EducacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_educacion')
    else:
        form = EducacionForm()
    return render(request, 'app_1/nueva_educacion.html', {'form': form})

def listar_experiencia(request):
    experiencias = Experiencia.objects.all()
    return render(request, 'app_1/listar_experiencia.html', {'experiencias': experiencias})

def nueva_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_experiencia')
    else:
        form = ExperienciaForm()
    return render(request, 'app_1/nueva_experiencia.html', {'form': form})
