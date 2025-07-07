from django import forms
from .models import Pais, Estado, Cidade, Empresa, EstadoCivil, Escolaridade

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do país'}),
            'codigo_iso2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código ISO 2'}),
            'codigo_iso3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código ISO 3'}),
            'ddi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código DDI'}),
            'codigo_siscomex': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código Siscomex'}),
            'continente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Continente'}),
        }

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do estado'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sigla UF'}),
            'pais': forms.Select(attrs={'class': 'form-select'}),
            'codigo_ibge': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código IBGE'}),
            'regiao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Região'}),
        }

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da cidade'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'codigo_ibge': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código IBGE'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP Inicial'}),
        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da empresa'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'site': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Site'}),
            'data_fundacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class EstadoCivilForm(forms.ModelForm):
    class Meta:
        model = EstadoCivil
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do estado civil'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição', 'rows': 3}),
        }

class EscolaridadeForm(forms.ModelForm):
    class Meta:
        model = Escolaridade
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da escolaridade'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição', 'rows': 3}),
        }

class EscolaridadeForm(forms.ModelForm):
    class Meta:
        model = Escolaridade
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da escolaridade'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição', 'rows': 3}),
        }
