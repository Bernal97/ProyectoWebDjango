from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto

class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class': 'usuario'}), max_length=150, required=True)
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), max_length=30, required=True)
    password2 = forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(), max_length=30, required=True)
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'email'}), max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ContactoForm(forms.Form):
        name = forms.CharField(label = 'Nombre',max_length= 30, widget = forms.TextInput, required = True)
        email = forms.CharField(label = 'E-mail',max_length = 30, widget = forms.TextInput, required = True)
        mensaje = forms.CharField(widget = forms.Textarea, required = True)
        
class CategoriaForm(forms.Form):
    nombreCate = forms.CharField(widget = forms.TextInput)