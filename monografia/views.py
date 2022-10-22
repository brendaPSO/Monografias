from multiprocessing import context
from django.shortcuts import render, redirect

from monografia.Filters import MonografiaFilter

from . models import Monografia

from . forms import MonografiaForm

# Create your views here.
def index(request):
    #Lista todas
    monografia = Monografia.objects.all()
    context = {
        'lista': monografia
    }
    return render(request,'monografia.html', context)


def monografia_filter_list(request):
    object_list = Monografia.objects.all()
    monografia_list = MonografiaFilter(request.GET, queryset=object_list)

    context = {
        'object_list': object_list,
        'filter':  monografia_list
    }
    return render(request,'monografia_pesquisar.html', context)


def adicionar(request):
    form = MonografiaForm()
    if request.method == "POST":
        form = MonografiaForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = MonografiaForm()
            #return render(request, 'adicionar_monografia.html', {'form': form})
            return redirect('monografia_index')
        else:
            form = MonografiaForm()

    return render (request, 'adicionar_monografia.html', {'form': form})