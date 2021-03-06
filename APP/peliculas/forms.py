from .models import Pelicula, Usuario
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class PeliculaForm(ModelForm):
    nombre = forms.CharField(max_length=100, required=True)
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if(Pelicula.objects.filter(nombre=nombre) ):
            raise ValidationError('Ya existe la pelicula')
        return nombre
    class Meta:
        model = Pelicula
        fields = '__all__'
class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=15,required=True)
    first_name = forms.CharField(max_length=15,required=True)
    last_name = forms.CharField(max_length=15,required=True)
    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name')

class PerfilForm(ModelForm):
    domicilio = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=10)
    fecha_de_nacimiento = forms.DateField()
    
    class Meta:
        model = Usuario
        fields = ('domicilio','telefono','fecha_de_nacimiento')
