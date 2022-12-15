from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm
import requests
import json

# Create your views here.
def index(request):
    api = "http://127.0.0.1:8000/api/pessoa/"
    pessoas = requests.get(api)
    try:
        lista = pessoas.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")
    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor
    context = {
        "lista" : dicionario
    }
    return render(request, 'core_index.html', context)

def adicionar(request):
    form = PessoaForm()
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            r = requests.post("http://127.0.0.1:8000/api/pessoa/", json=form.cleaned_data)
            #post = form.save()
            #post.save()
            #form = PessoaForm()
            r.status_code
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