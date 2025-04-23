from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['hora_entrada', 'data_entrada', 'nome', 'produto_id', 'quantidade', 'empresa']
        widgets = {
            'hora_entrada': forms.TimeInput(attrs={'type': 'time'}),
            'data_entrada': forms.DateInput(attrs={'type': 'date'}),
        }