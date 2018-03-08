from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    template_name = 'CRUDs/jogos_digitais/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        jogos_digitais = JogosDigitais.objects.all().order_by('codigo')
        if codigo:
            jogos_digitais = jogos_digitais.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/jogos_digitais/index.html',
            { 'jogos_digitais' : jogos_digitais}
        )

class novo_alterar(View):
    template_name = 'CRUDs/jogos_digitais/novo_alterar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = JogosDigitais.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )
    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = JogosDigitais.objects.get(codigo=codigo)
        form = JogosDigitais_Form(request.POST, instance=item)
        if form.is_valid():
            if item:
                form.save(request.POST)
            else:
                form.save(request.POST)
            return redirect('jogos_digitais_index')
        else:
            return render(
                request,
                self.template_name,
                {'item':item,
                 'form':form}
            )

class deletar(View):
    template_name = 'CRUDs/jogos_digitais/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = JogosDigitais.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = JogosDigitais.objects.get(codigo=codigo)
        item.delete()
        return redirect('jogos_digitais_index')