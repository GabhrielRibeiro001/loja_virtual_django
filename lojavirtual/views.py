from django.shortcuts import render, redirect
from . models import Produto
from . forms import ProdutoForm



# Create your views here.

def home(request):

   
    lista_produto = Produto.objects.all()
    pesquisa = request.GET.get('cat')
    busca = request.GET.get('q')


    if pesquisa and pesquisa != 'Todos':
        lista_produto = Produto.objects.filter(categoria__titulo=pesquisa)

    if busca:
         lista_produto = Produto.objects.filter(titulo__icontains=busca)

    return render(request, 'index.html', {
        'lista_produto': lista_produto, 
    })

def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    return render(request, 'produto.html', {'produto':produto})


def carinho(request):
    return render(request, 'carinho.html')


def painel(request):
    if request.method == 'POST':
        formulario = ProdutoForm(request.POST, request.FILES) 
        if formulario.is_valid():
            formulario.save()
            return redirect("obrigado")

    else:

        formulario = ProdutoForm()   
    return render(request, 'painel.html', {'formulario': formulario})