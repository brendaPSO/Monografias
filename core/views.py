from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.
def index(request):
    pessoas = Pessoa.objects.all()
    context = {
        'lista': pessoas
    }
    return render(request, 'core_index.html', context)

def adicionar(request):
    form = PessoaForm()
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = PessoaForm()
            #return render(request, 'core_adicionar.html', {'form' : form})
            return redirect('core_index')
        else:
            form = PessoaForm()

    return render(request, 'core_adicionar.html', {'form' : form})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('core_index')

    return render(request, 'core_adicionar.html', {'form' : form, 'pessoa': pessoa})

def apagar(request, id):
    pessoa = Pessoa.objects.get(id=id)

    if request.method== 'POST':
        pessoa.delete()
        return redirect('core_index')

    return render(request, "core_apagar_confirma.html", {'pessoa': pessoa})