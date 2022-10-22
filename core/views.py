from django.shortcuts import render, redirect
from .models import Pessoa


def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core_index.html', {"pessoas": pessoas})


def salvar(request):
    r_nome = request.POST.get('nome')
    r_tipo = request.POST.get('tipo')
    r_curso = request.POST.get('curso')
    r_universidade = request.POST.get('universidade')
    r_email = request.POST.get('email')
    r_curriculo = request.POST.get('curriculo')
    r_google_scholar = request.POST.get('google_scholar')
    r_research_gate = request.POST.get('research_gate')
    r_linkedin = request.POST.get('linkedin')
    r_orcid = request.POST.get('orcid')
    r_github = request.POST.get('github')

    Pessoa.objects.create(
        nome=r_nome,
        tipo=r_tipo,
        curso=r_curso,
        universidade=r_universidade,
        email=r_email,
        curriculo=r_curriculo,
        google_scholar=r_google_scholar,
        research_gate=r_research_gate,
        linkedin=r_linkedin,
        orcid=r_orcid,
        github=r_github,
    )

    pessoas = Pessoa.objects.all()

    return render(request, 'core_index.html', {"pessoas": pessoas})


def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'update.html', {"pessoa": pessoa})


def update(request, id):
    novoNome = request.POST.get('nome')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = novoNome
    pessoa.save()
    return redirect(home)


def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)
