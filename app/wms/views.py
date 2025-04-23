from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import ProdutoForm

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_sucesso')
    else:
        form = ProdutoForm()
    
    return render(request, 'wms/pages/cadastrar_produto.html', {'form': form})

def produto_sucesso(request):
    return render(request, 'wms/pages/sucesso.html')

def index(request):
    return render(
        request, 
        'wms/pages/index.html'
    )