from multiprocessing import context
from django.shortcuts import render, redirect
from monografia.Filters import MonografiaFilter
from . models import Monografia
from . forms import MonografiaForm

# Create your views here.
def index(request):
    monografias = Monografia.objects.all()
    context = {
        'lista': monografias
    }
    return render(request, 'monografia_index.html', context)

def adicionar(request):
    form = MonografiaForm()
    if request.method == "POST":
        form = MonografiaForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = MonografiaForm()
            #return render(request, 'monografia_adicionar.html', {'form' : form})
            return redirect('monografia_index')
        else:
            form = MonografiaForm()

    return render(request, 'monografia_adicionar.html', {'form' : form})

def editar(request, id):
    monografia = Monografia.objects.get(id=id)
    form = MonografiaForm(request.POST or None, instance=monografia)

    if form.is_valid():
        form.save()
        return redirect('monografia_index')

    return render(request, 'monografia_adicionar.html', {'form' : form, 'monografia': monografia})

def apagar(request, id):
    monografia = Monografia.objects.get(id=id)

    if request.method== 'POST':
        monografia.delete()
        return redirect('monografia_index')

    return render(request, "monografia_apagar_confirma.html", {'monografia': monografia})
    
def monografia_filter_list(request):
    object_list = Monografia.objects.all()
    monografia_list = MonografiaFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter':  monografia_list
    }
    return render(request,'monografia_pesquisar.html', context)