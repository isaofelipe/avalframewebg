from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    template_name = 'CRUDs/aprendizagens/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        aprendizagens = Aprendizagens.objects.all().order_by('codigo')
        if codigo:
            aprendizagens = aprendizagens.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/aprendizagens/index.html',
            { 'aprendizagens' : aprendizagens}
        )

class novo_alterar(View):
    template_name = 'CRUDs/aprendizagens/novo_alterar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        aprendizagem = None
        tipo = None
        if codigo:
            aprendizagem = Aprendizagens.objects.get(codigo=codigo)
            if aprendizagem.tipo == 'A': tipo='Atitude'
            elif aprendizagem.tipo == 'H': tipo='Habilidade'
            elif aprendizagem.tipo == 'C': tipo="Conhecimento"
            else: aprendizagem.tipo == None
        return render(
            request,
            self.template_name,
            {'aprendizagem':aprendizagem,
                'tipo':tipo,
            }
        )
    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        aprendizagem = None
        if codigo:
            aprendizagem = Aprendizagens.objects.get(codigo=codigo)
        form = Aprendizagens_Form(request.POST, instance=aprendizagem)
        if form.is_valid():
            if aprendizagem:
                form.save(request.POST)
            else:
                form.save(request.POST)
            return redirect('aprendizagens_index')
        else:
            return render(
                request,
                self.template_name,
                {'aprendizagem':aprendizagem,
                 'form':form}
            )

class deletar(View):
    template_name = 'CRUDs/aprendizagens/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        aprendizagem = Aprendizagens.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'aprendizagem':aprendizagem}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        aprendizagem = Aprendizagens.objects.get(codigo=codigo)
        aprendizagem.delete()
        return redirect('aprendizagens_index')