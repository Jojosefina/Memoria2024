from datetime import date
from django import forms
from .models import Asignaturas, Documentos, Etiquetas, Profesores, TiposMaterial, Account, Comentarios
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


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


def validate_uchile_email(value):
    if not any(value.endswith(domain) for domain in ["@ug.uchile.cl", "@uchile.cl", "@ing.uchile.cl"]):
        raise ValidationError(
            "El correo debe terminar en @ug.uchile.cl, @uchile.cl o @ing.uchile.cl")


class RegisterForm(UserCreationForm):
    correo = forms.EmailField(validators=[
                              validate_uchile_email], widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ['nombre', 'apellido', 'correo',
                  'password1', 'password2', 'fecha_nacimiento', 'fecha_ingreso']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_ingreso'].initial = '2018-03-03'

        # Calcula el año mínimo permitido (hace 17 años)
        today = date.today()
        max_birthyear = today.year - 17

        # Actualiza los atributos del widget de fecha_nacimiento
        self.fields['fecha_nacimiento'].widget.attrs.update({
            'max': f'{max_birthyear}-12-31',
            'class': 'form-control',
            'type': 'date'
        })

    def clean_email(self):
        email = self.cleaned_data['correo'].lower()
        try:
            account = Account.objects.exclude(
                pk=self.instance.pk).get(correo=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError(
            'Correo "%s" ya está en uso.' % account.correo)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu comentario aquí...'}),
        }


class RateForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['calificacion']
        widgets = {
            'calificacion': forms.NumberInput(attrs={'type': 'range', 'class': 'form-range', 'min': '1', 'max': '5', 'step': '1'}),
        }
