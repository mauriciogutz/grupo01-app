from django import forms
from .models import Promocion, Condiciones, DetalleVenta, Venta
class PromocionForm(forms.ModelForm):
    # Definir las opciones para el campo tipomonto
    TIPO_MONTO_CHOICES = [
        (1, 'CANTIDAD'),
        (2, 'MONTO'),
    ]

    # Usar el widget Select y proporcionar las opciones
    tipomonto = forms.ChoiceField(choices=TIPO_MONTO_CHOICES, label='Tipo de Monto')

    class Meta:
        model = Promocion
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class CondicionesForms(forms.ModelForm):
    class Meta:
        model = Condiciones
        exclude = ['promocion']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'fecha_venta': forms.DateInput(attrs={'type': 'date'}),
        }

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        exclude = ['venta']