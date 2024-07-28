from django import forms
from .models import Proyecto, Habilidad, Educacion, Experiencia

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin']

class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['nombre', 'nivel']

class EducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
        fields = ['institucion', 'titulo', 'fecha_inicio', 'fecha_fin', 'descripcion']

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['empresa', 'puesto', 'fecha_inicio', 'fecha_fin', 'descripcion']

class BuscarPersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)