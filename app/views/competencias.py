from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    template_name = 'CRUDs/competencias/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        competencias = Competencias.objects.all().order_by('codigo')
        if codigo:
            competencias = competencias.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/competencias/index.html',
            { 'competencias' : competencias}
        )

class novo_alterar(View):
    template_name = 'CRUDs/competencias/novo_alterar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        competencia = None
        if codigo:
            competencia = Competencias.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'competencia':competencia}
        )
    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        competencia = None
        if codigo:
            competencia = Competencias.objects.get(codigo=codigo)
        form = Competencias_Form(request.POST, instance=competencia)
        if form.is_valid():
            if competencia:
                form.save(request.POST)
            else:
                form.save(request.POST)
            return redirect('competencias_index')
        else:
            return render(
                request,
                self.template_name,
                {'competencia':competencia,
                 'form':form}
            )

class deletar(View):
    template_name = 'CRUDs/competencias/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        competencia = Competencias.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'competencia':competencia}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        competencia = Competencias.objects.get(codigo=codigo)
        competencia.delete()
        return redirect('competencias_index')