from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget 
from .models import Producto, Cliente


class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['Idproducto', 'nombre', 'marca', 'precio']
        labels ={
            'Idproducto': 'Idproducto', 
            'nombre': 'nombre', 
            'marca': 'marca', 
            'precio': 'precio',
        }
        widgets={
            'Idproducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Idproducto', 
                    'id': 'Idproducto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'precio': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'precio',
                }
            )

        }

    class ClienteForm(forms.ModelForm):

      class Meta: 
        model= Cliente
        fields = ['rut', 'nombre', 'informacion']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'informacion': 'Informacion', 
            
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'informacion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese informacion', 
                    'id': 'informacion'
                }
            ),

            

        }
