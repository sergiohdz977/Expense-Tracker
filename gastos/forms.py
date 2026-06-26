from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'


class FiltroFechaForm(forms.Form):
    desde = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
    required=False
    )
    hasta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
    required=False
    )