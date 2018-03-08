from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *
from django.shortcuts import render_to_response
import json
import re


class index(View):
    template_name = 'carga_aprendizagens/index.html'

    def get(self, request, *args, **kwargs):
        form = UploadFileForm()
        return render(
            request,
            'carga_aprendizagens/index.html',
            {'form':form},
        )
    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['file']
            lista = []
            for linha in arquivo:
                instancia = re.split(" '|' | |\r\n",linha.decode())
                item = HistoricoRegistro(codigo_jogador=instancia[0], data_inicio_jogo=instancia[1], hora_inicio_jogo=instancia[2], codigo_jogo=instancia[3], nivel_jogo=instancia[4], fase_jogo=instancia[5], etapa_jogo=instancia[6], tipo_aeej=instancia[7], codigo_aeej=instancia[8], valor1=instancia[9], valor2=instancia[10], valor3=instancia[11], data_gravacao=instancia[12], hora_gravacao=instancia[13], nome_arquivo=instancia[14])
                lista.append(item)
                item.save()
            processa_aprendizagens(lista)
            return render(
                request,
                'carga_aprendizagens/index.html',
                {
                    'form':form,
                    'teste':arquivo
                },
            )
        else:
            return render(
                request,
                'carga_aprendizagens/index.html',
                {'form':form},
            )
        
def processa_aprendizagens(lista):
    verificador = lista[0]
    lista_aprendizagem_aeej = []
    for instancia in lista:
        if (not(verificador.codigo_jogador == instancia.codigo_jogador and verificador.data_inicio_jogo == instancia.data_inicio_jogo
            and verificador.hora_inicio_jogo == instancia.hora_inicio_jogo and verificador.codigo_jogo == instancia.codigo_jogo)):
            lista_base_consolidada = processa_aluno(lista_aprendizagem_aeej, verificador)
            for i in lista_base_consolidada:
                i.save()
            lista_aprendizagem_aeej = []
            verificador = instancia

        aprendizagensAeej = AprendizagensAeej.objects.filter(codigo_jogo = instancia.codigo_jogo, nivel_jogo = instancia.nivel_jogo, fase_jogo = instancia.fase_jogo,
                etapa_jogo = instancia.fase_jogo, codigo_aeej= instancia.codigo_aeej)
        for i in aprendizagensAeej:
            lista_aprendizagem_aeej.append(i)
    lista_base_consolidada = processa_aluno(lista_aprendizagem_aeej, verificador)
    for i in lista_base_consolidada:
        i.save()

         
def processa_aluno(lista_aprendizagem_aeej, verificador):
    lista_todas_aprendizagens_aeej = AprendizagensAeej.objects.filter(codigo_jogo = verificador.codigo_jogo)
    lista_aprendizagem_valor = {}
    for i in lista_todas_aprendizagens_aeej:
        lista_aprendizagem_valor[i.codigo_aprendizagem] = 0
    for i in lista_aprendizagem_aeej:
        valor_anterior = lista_aprendizagem_valor[i.codigo_aprendizagem]
        if i.descritor_operacao == '+':
            lista_aprendizagem_valor[i.codigo_aprendizagem] = valor_anterior + (i.valor_padrao * contribuicao_do_aeej_na_aprendizagem)
        elif i.descritor_operacao == '-':
            lista_aprendizagem_valor[i.codigo_aprendizagem] = valor_anterior - (i.valor_padrao * contribuicao_do_aeej_na_aprendizagem)
        elif i.descritor_operacao == '*':
            lista_aprendizagem_valor[i.codigo_aprendizagem] = valor_anterior * (i.valor_padrao * contribuicao_do_aeej_na_aprendizagem)
        elif i.descritor_operacao == '/':
            lista_aprendizagem_valor[i.codigo_aprendizagem] = valor_anterior / (i.valor_padrao * contribuicao_do_aeej_na_aprendizagem)
        valor_maximo = Aprendizagens.objects.get(pk = i.codigo_aprendizagem).valor_maximo
        if lista_aprendizagem_valor[i.codigo_aprendizagem] > valor_maximo:
            lista_aprendizagem_valor[i.codigo_aprendizagem] = valor_maximo
        if lista_aprendizagem_valor[i.codigo_aprendizagem] < 0:
            lista_aprendizagem_valor[i.codigo_aprendizagem] = 0

    lista_base_consolidada = []
    for i in lista_aprendizagem_valor:
        lista_base_consolidada.append(BaseConsolidada(codigo_jogador = verificador.codigo_jogador, data_inicio_jogo = verificador.data_inicio_jogo, hora_inicio_jogo = verificador.hora_inicio_jogo, 
                                                      codigo_jogo = verificador.codigo_jogo, codigo_aprendizagem = i, valor_aprendizagem = lista_aprendizagem_valor[i]))
    
    return lista_base_consolidada