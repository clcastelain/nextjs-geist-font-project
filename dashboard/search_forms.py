from django import forms
from .models import Estado

class PaisSearchForm(forms.Form):
    nome = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do país'}))
    continente = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Continente'}))

class EstadoSearchForm(forms.Form):
    nome = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do estado'}))
    sigla = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sigla UF'}))
    regiao = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Região'}))

class CidadeSearchForm(forms.Form):
    nome = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da cidade'}))
    estado = forms.ModelChoiceField(
        required=False,
        queryset=Estado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Selecione um estado"
    )
