from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    template_name = 'CRUDs/competencias_aprendizagens/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        competencias_aprendizagens = CompetenciasAprendizagens.objects.all().order_by('codigo')
        if codigo:
            competencias_aprendizagens = competencias_aprendizagens.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/competencias_aprendizagens/index.html',
            { 'competencias_aprendizagens' : competencias_aprendizagens}
        )

class novo_alterar(View):
    template_name = 'CRUDs/competencias_aprendizagens/novo_alterar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = CompetenciasAprendizagens.objects.get(codigo=codigo)
        form = CompetenciasAprendizagens_Form(instance=item)
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
            item = CompetenciasAprendizagens.objects.get(codigo=codigo)
        form = CompetenciasAprendizagens_Form(request.POST, instance=item)
        if form.is_valid():
            if item:
                form.save(request.POST)
            else:
                form.save(request.POST)
            return redirect('competencias_aprendizagens_index')
        else:
            return render(
                request,
                self.template_name,
                {'item':item,
                 'form':form}
            )

class deletar(View):
    template_name = 'CRUDs/competencias_aprendizagens/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = CompetenciasAprendizagens.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = CompetenciasAprendizagens.objects.get(codigo=codigo)
        item.delete()
        return redirect('competencias_aprendizagens_index')