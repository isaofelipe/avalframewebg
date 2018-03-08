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
    template_name = 'CRUDs/aprendizagens_aeej/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        aprendizagens_aeej = AprendizagensAeej.objects.all().order_by('codigo')
        if codigo:
            aprendizagens_aeej = aprendizagens_aeej.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/aprendizagens_aeej/index.html',
            { 'aprendizagens_aeej' : aprendizagens_aeej}
        )

class novo_alterar(View):
    template_name = 'CRUDs/aprendizagens_aeej/novo_alterar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = AprendizagensAeej.objects.get(codigo=codigo)
        form = AprendizagensAeej_Form(instance=item)
        return render(
            request,
            self.template_name,
            {
                'item':item,
                'form':form,
            }
        )
    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = AprendizagensAeej.objects.get(codigo=codigo)
        form = AprendizagensAeej_Form(request.POST, instance=item)
        if form.is_valid():
            form.save(request.POST)
            return redirect('aprendizagens_aeej_index')
        else:
            return render(
                request,
                self.template_name,
                {'item':item,
                 'form':form}
            )

class deletar(View):
    template_name = 'CRUDs/aprendizagens_aeej/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = AprendizagensAeej.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = AprendizagensAeej.objects.get(codigo=codigo)
        item.delete()
        return redirect('aprendizagens_aeej_index')

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

def buscar_fases(request):
    codigo_nivel = request.GET.get('nivel_jogo', None)
    fases = FasesJogo.objects.filter(codigo_nivel = codigo_nivel)
    opcoes = []
    for fase in fases:
        opcoes.append({'codigo':fase.codigo,
                       'fase':fase.fase,
                       'titulo':fase.titulo,
                       })
    data = {
        'opcoes' : opcoes,
    }
    return JsonResponse(data)

def buscar_etapas(request):
    codigo_etapa = request.GET.get('etapa_jogo', None)
    etapas = EtapasJogo.objects.filter(codigo_etapa = codigo_etapa)
    opcoes = []
    for etapa in etapas:
        opcoes.append({'codigo':etapa.codigo,
                       'fase':etapa.etapa,
                       'titulo':etapa.titulo,
                       })
    data = {
        'opcoes' : opcoes,
    }
    return JsonResponse(data)