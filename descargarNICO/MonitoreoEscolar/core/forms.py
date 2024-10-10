from django import forms
from .models import Curso
from .models import Asignatura

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['id_curso', 'seccion', 'anno_generacion', 'semestre']



class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['id_asignatura', 'nombre_asignatura']