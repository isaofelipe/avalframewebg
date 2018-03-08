from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    template_name = 'CRUDs/niveis_aprendizagem/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        niveis_aprendizagem = NiveisAprendizagem.objects.all().order_by('codigo')

        if codigo:
            niveis_aprendizagem = niveis_aprendizagem.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/niveis_aprendizagem/index.html',
            { 'niveis_aprendizagem' : niveis_aprendizagem}
        )

class novo_alterar(View):
    template_name = 'CRUDs/niveis_aprendizagem/novo_alterar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = NiveisAprendizagem.objects.get(codigo=codigo)
        form = NiveisAprendizagem_Form(instance = item)
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
            item = NiveisAprendizagem.objects.get(codigo=codigo)
        form = NiveisAprendizagem_Form(request.POST, instance=item)
        if form.is_valid():
            if item:
                form.save(request.POST)
            else:
                form.save(request.POST)
            return redirect('niveis_aprendizagem_index')
        else:
            return render(
                request,
                self.template_name,
                {'item':item,
                 'form':form}
            )

class deletar(View):
    template_name = 'CRUDs/niveis_aprendizagem/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = NiveisAprendizagem.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = NiveisAprendizagem.objects.get(codigo=codigo)
        item.delete()
        return redirect('niveis_aprendizagem_index')