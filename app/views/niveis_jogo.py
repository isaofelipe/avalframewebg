from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    template_name = 'CRUDs/niveis_jogo/index.html'

    def get(self, request, *args, **kwargs):
        codigo_jogo = request.GET.get('codigo_jogo', None)
        niveis_jogo = NiveisJogo.objects.all().order_by('codigo_jogo')
        if codigo_jogo:
            jogo_digital = JogosDigitais.objects.filter(codigo = codigo_jogo)
            niveis_jogo = niveis_jogo.filter(codigo_jogo = jogo_digital)
        return render(
            request,
            'CRUDs/niveis_jogo/index.html',
            { 'niveis_jogo' : niveis_jogo}
        )

class novo_alterar(View):
    template_name = 'CRUDs/niveis_jogo/novo_alterar.html'
    jogos = JogosDigitais.objects.all()

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = NiveisJogo.objects.get(codigo=codigo)
        form = NiveisJogo_Form(instance=item)
        return render(
            request,
            self.template_name,
            {
                'item':item,
                'jogos':self.jogos,
                'form':form,
            }
        )
    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = NiveisJogo.objects.get(codigo=codigo)
        form = NiveisJogo_Form(request.POST, instance=item)
        if form.is_valid():
            form.save(request.POST)
            return redirect('niveis_jogo_index')
        else:
            return render(
                request,
                self.template_name,
                {
                    'item':item,
                    'form':form,
                    'jogos':self.jogos,
                    
                }
            )

class deletar(View):
    template_name = 'CRUDs/niveis_jogo/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = NiveisJogo.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = NiveisJogo.objects.get(codigo=codigo)
        item.delete()
        return redirect('niveis_jogo_index')