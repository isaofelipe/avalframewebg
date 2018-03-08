from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *
from json import *
from django.http import JsonResponse
from datetime import date
from sklearn import tree
import pandas as pd
import numpy as np


class index(View):
    template_name = 'CRUDs/jogadores/index.html'

    def get(self, request, *args, **kwargs):
        codigo = request.GET.get('codigo', None)
        jogadores = Jogadores.objects.all().order_by('codigo')
        if codigo:
            jogadores = jogadores.filter(codigo = codigo)
        return render(
            request,
            'CRUDs/jogadores/index.html',
            { 'jogadores' : jogadores}
        )

class novo_alterar(View):
    template_name = 'CRUDs/jogadores/novo_alterar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = Jogadores.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )
    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = None
        if codigo:
            item = Jogadores.objects.get(codigo=codigo)
        form = Jogadores_Form(request.POST, instance=item)
        if form.is_valid():
            if item:
                form.save(request.POST)
            else:
                form.save(request.POST)
            return redirect('jogadores_index')
        else:
            return render(
                request,
                self.template_name,
                {'item':item,
                 'form':form}
            )

class deletar(View):
    template_name = 'CRUDs/jogadores/deletar.html'

    def get(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = Jogadores.objects.get(codigo=codigo)
        return render(
            request,
            self.template_name,
            {'item':item}
        )

    def post(self, request, *args, **kwargs):
        codigo = kwargs.get('codigo', None)
        item = Jogadores.objects.get(codigo=codigo)
        item.delete()
        return redirect('jogadores_index')
        
def gerar_perfil(request):
    sexo = request.GET.get('sexo', None)
    data_nascimento = request.GET.get('data_nascimento', None)
    data_desde_quando_joga = request.GET.get('data_desde_quando_joga', None)
    coeficiente_de_rendimento = request.GET.get('coeficiente_de_rendimento', None)
    tipo_jogo_preferido = request.GET.get('tipo_jogo_preferido', None)
    
    idade = calcula_idade(data_nascimento)
    ano_desde_quando_joga = datetime.strptime(data_desde_quando_joga, '%Y-%m-%d').date().year
    coeficiente_de_rendimento = int(coeficiente_de_rendimento)
    
    retorno = classifica(sexo, idade, ano_desde_quando_joga, coeficiente_de_rendimento, tipo_jogo_preferido)
    data = {
        'retorno' : retorno,
    }
    return JsonResponse(data)
    
def calcula_idade(data):
    print (data)
    data = datetime.strptime(data, '%Y-%m-%d').date()
    hoje = date.today()
    return hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))
    
    
#------------------------------------------------------------------------------------------------------------------------------------------    



def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x=0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1
            df[column] = list(map(convert_to_int, df[column]))
    return df

def classifica(sexo,idade,data_desde_quando_joga,coeficiente_de_rendimento,tipo_jogo_preferido):
    
    alun = pd.read_csv('app/views/teste19.csv',delimiter=',')
    
    alun = handle_non_numerical_data(alun)
    
    alun.data = alun.values[:,0:5]
    alun.target = alun.values[:,5]
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(alun.data,alun.target)
    
    
    
    vet = []
    
    if(sexo is 'M'):
        vet.append(0)
    else:
        vet.append(1)
        
    vet.append(idade)
    vet.append(data_desde_quando_joga)
    vet.append(coeficiente_de_rendimento)
    
    vet.append(tipo_jogo_preferido)
    
    resultado = clf.predict([vet])
    return int(resultado[0])



'''
M-0
F-1
------------
FPS-0
PILOTAGEM-1
SOCIALIZACAO-2
RPG-3
EXPLORACAO-4
-------------
RESULTADO:
muitoFacil-0
facil-3
medio-4
dificil-2
muitoDificil-1

'''


