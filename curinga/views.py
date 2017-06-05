# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Contato
from .forms import ContatoForm


def index(request):
    contatos = Contato.objects.all()

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ContatoForm()

    return render(request, 'curinga/index.html', {
        'contatos': contatos,
        'form': form
    })


def details(request, id):
    contato = get_object_or_404(Contato, id=id)
    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'curinga/detail.html', {
        'contato': contato,
        'form': form,
    })


def delete(request, id):
    contato = get_object_or_404(Contato, id=id)
    if request.method == 'GET':
        contato.delete()
        return redirect('index')
    return render(request, {'object': contato})
