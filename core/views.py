from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    Mensalista,
    MovMensalista
)
from .forms import (
    PessoaForm, 
    VeiculoForm, 
    MovRotativoForm, 
    MensalistaForm,
    MovMensalistaForm
)

@login_required(login_url='/accounts/login/')
def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)

#===========================PESSOAS==================================
@login_required(login_url='/accounts/login/')
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


@login_required(login_url='/accounts/login/')
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required(login_url='/accounts/login/')
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required(login_url='/accounts/login/')
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'objDelete': pessoa})


#===========================VEÍCULOS==================================


@login_required(login_url='/accounts/login/')
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


@login_required(login_url='/accounts/login/')
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required(login_url='/accounts/login/')
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required(login_url='/accounts/login/')
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'objDelete': veiculo})


#===========================MOVIMENTO ROTATIVOS==================================


@login_required(login_url='/accounts/login/')
def lista_movRotativos(request):
    movRotativos = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'movRotativos': movRotativos, 'form': form}
    return render(request, 'core/lista_movRotativos.html', data)


@login_required(login_url='/accounts/login/')
def movRotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movRotativos')


@login_required(login_url='/accounts/login/')
def movRotativo_update(request, id):
    data = {}
    movRotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movRotativo)
    data['movRotativo'] = movRotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movRotativos')
    else:
        return render(request, 'core/update_movRotativo.html', data)


@login_required(login_url='/accounts/login/')
def movRotativo_delete(request, id):
    movRotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movRotativo.delete()
        return redirect('core_lista_movRotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'objDelete': movRotativo})


#===========================MENSALISTAS==================================


@login_required(login_url='/accounts/login/')
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)


@login_required(login_url='/accounts/login/')
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required(login_url='/accounts/login/')
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required(login_url='/accounts/login/')
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'objDelete': mensalista})


#===========================MOVIMENTO MENSALISTAS==================================


@login_required(login_url='/accounts/login/')
def lista_movMensalistas(request):
    movMensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'movMensalistas': movMensalistas, 'form': form}
    return render(request, 'core/lista_movMensalistas.html', data)


@login_required(login_url='/accounts/login/')
def movMensalistas_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movMensalistas')


@login_required(login_url='/accounts/login/')
def movMensalista_update(request, id):
    data = {}
    movMensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movMensalista)
    data['movMensalista'] = movMensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movMensalistas')
    else:
        return render(request, 'core/update_movMensalista.html', data)


@login_required(login_url='/accounts/login/')
def movMensalista_delete(request, id):
    movMensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movMensalista.delete()
        return redirect('core_lista_movMensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'objDelete': movMensalista})