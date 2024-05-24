from django import forms
from .models import Asignaturas, Documentos, Etiquetas, Profesores, TiposMaterial, Account


class FileForm(forms.ModelForm):
    # campo de etiquetas debe ser multiselect tipo checkbox y todo el contenedor debe poseer el estilo custom-upload-bar
    etiquetas = forms.ModelMultipleChoiceField(
        queryset=Etiquetas.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}), required=True)

    class Meta:
        model = Documentos
        fields = ['titulo', 'id_tipo_material',
                  'id_asignaturas', 'profesor', 'archivo', 'etiquetas']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control custom-upload-bar'}),
            'id_tipo_material': forms.Select(attrs={'class': 'form-control custom-upload-bar'}),
            'id_asignaturas': forms.Select(attrs={'class': 'form-control custom-upload-bar'}),
            'profesor': forms.Select(attrs={'class': 'form-control custom-upload-bar'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control custom-upload-file-select'}),
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['nombre', 'apellido', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }
