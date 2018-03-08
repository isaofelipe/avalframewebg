from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    template_name = 'CRUDs/fases_jogo/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        fases_jogo = FasesJogo.objects.all().order_by('codigo')
        if codigo:
            fases_jogo = fases_jogo.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/fases_jogo/index.html',
            { 'fases_jogo' : fases_jogo}
        )

class novo_alterar(View):
    template_name = 'CRUDs/fases_jogo/novo_alterar.html'
    jogos = JogosDigitais.objects.all()

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = FasesJogo.objects.get(codigo=codigo)
        form = FasesJogo_Form(instance = item)
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
            item = FasesJogo.objects.get(codigo=codigo)
        form = FasesJogo_Form(request.POST, instance=item)
        if form.is_valid():
            form.save(request.POST)
            return redirect('fases_jogo_index')
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
    template_name = 'CRUDs/fases_jogo/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = FasesJogo.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = FasesJogo.objects.get(codigo=codigo)
        item.delete()
        return redirect('fases_jogo_index')

def buscar_niveis(request):
    codigo_jogo = request.GET.get('codigo_jogo', None)
    niveis = NiveisJogo.objects.filter(codigo_jogo = codigo_jogo)
    opcoes = []
    for nivel in niveis:
        opcoes.append({'codigo':nivel.codigo,
                       'nivel':nivel.nivel,
                       'titulo':nivel.titulo,
                       })
    data = {
        'opcoes' : opcoes,
    }
    return JsonResponse(data)