from multiprocessing import context
from django.shortcuts import render, redirect

from . models import Monografia

from . forms import MonografiaForm

# Create your views here.
def index(request):
    #Consulta
    monografia = Monografia.objects.all()
    context = {
        'lista': monografia
    }
    return render(request,'monografia.html', context)

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