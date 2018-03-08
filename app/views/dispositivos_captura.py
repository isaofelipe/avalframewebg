from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    template_name = 'CRUDs/dispositivos_captura/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        dispositivos_captura = DispositivosCaptura.objects.all().order_by('codigo')
        if codigo:
            dispositivos_captura = dispositivos_captura.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/dispositivos_captura/index.html',
            { 'dispositivos_captura' : dispositivos_captura}
        )

class novo_alterar(View):
    template_name = 'CRUDs/dispositivos_captura/novo_alterar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = DispositivosCaptura.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )
    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = DispositivosCaptura.objects.get(codigo=codigo)
        form = DispositivosCaptura_Form(request.POST, instance=item)
        if form.is_valid():
            if item:
                form.save(request.POST)
            else:
                form.save(request.POST)
            return redirect('dispositivos_captura_index')
        else:
            return render(
                request,
                self.template_name,
                {'item':item,
                 'form':form}
            )

class deletar(View):
    template_name = 'CRUDs/dispositivos_captura/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = DispositivosCaptura.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = DispositivosCaptura.objects.get(codigo=codigo)
        item.delete()
        return redirect('dispositivos_captura_index')