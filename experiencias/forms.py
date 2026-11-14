from django import forms
from experiencias.models import Categoria, Experiencia, Inscripcion


class CategoriaRegistroForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.CheckboxInput(),
        }


class ExperienciaRegistroForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['titulo', 'categoria', 'descripcion', 'precio', 'cupo_maximo', 'fecha_hora', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cupo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'estado': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(estado=True)
        if self.instance and self.instance.pk and self.instance.fecha_hora:
            self.fields['fecha_hora'].initial = self.instance.fecha_hora.strftime('%Y-%m-%dT%H:%M')


class ValoracionForm(forms.ModelForm):
    CALIFICACIONES = [
        (5, '5 - Excelente'),
        (4, '4 - Muy buena'),
        (3, '3 - Buena'),
        (2, '2 - Regular'),
        (1, '1 - Deficiente'),
    ]
    valoracion = forms.ChoiceField(choices=CALIFICACIONES, label='Calificación', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Inscripcion
        fields = ['valoracion', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }