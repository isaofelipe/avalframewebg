"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm, TextInput
from app.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

class Form_Bootstrap(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form_Bootstrap, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })

class Aeej_Form(Form_Bootstrap):
    class Meta:
        model = Aeej
        fields = ['tipo', 'descricao', 'codigo_dispositivo']
        
class Aprendizagens_Form(Form_Bootstrap):
    class Meta:
        model = Aprendizagens
        fields = ['tipo', 'titulo', 'valor_maximo']

class Competencias_Form(Form_Bootstrap):
    class Meta:
        model = Competencias
        fields = ['titulo', 'valor_maximo_pontos']

class NiveisCompetenciaAvaliacao_Form(Form_Bootstrap):
    class Meta:
        model = NiveisCompetenciaAvaliacao
        fields = ['codigo_competencia', 'titulo', 'inicio_nivel', 'fim_nivel', 'jogadores_nesse_nivel']

class NiveisAprendizagem_Form(Form_Bootstrap):
    class Meta:
        model = NiveisAprendizagem
        fields = ['nivel', 'codigo_aprendizagem', 'titulo', 'inicio_nivel', 'fim_nivel', 'jogadores_nesse_nivel']
        
class NiveisJogo_Form(Form_Bootstrap):
    class Meta:
        model = NiveisJogo
        fields = ['codigo_jogo', 'titulo', 'nivel']
        
class DispositivosCaptura_Form(Form_Bootstrap):
    class Meta:
        model = DispositivosCaptura
        fields = ['nome']
        
class JogosDigitais_Form(Form_Bootstrap):
    class Meta:
        model = JogosDigitais
        fields = ['titulo']
        
class Jogadores_Form(Form_Bootstrap):
    class Meta:
        model = Jogadores
        fields = ['nome', 'sexo', 'data_nascimento', 'data_desde_quando_joga', 'coeficiente_de_rendimento', 'tipo_jogo_preferido', 'perfil_recomendacao']
        
class AprendizagensAeej_Form(Form_Bootstrap):
    class Meta:
        model = AprendizagensAeej
        fields = ['codigo_aprendizagem', 'codigo_jogo', 'nivel_jogo', 'fase_jogo', 'etapa_jogo', 'codigo_aeej', 'tipo_operacao', 'descritor_operacao', 'valor_padrao', 'contribuicao_do_aeej_na_aprendizagem']
        
class CompetenciasAprendizagens_Form(Form_Bootstrap):
    class Meta:
        model = CompetenciasAprendizagens
        fields = ['codigo_competencia', 'codigo_aprendizagem', 'contribuicao_da_aprendizagem_na_competencia']
        
class EtapasJogo_Form(Form_Bootstrap):
    class Meta:
        model = EtapasJogo
        fields = ['etapa', 'codigo_jogo', 'codigo_nivel', 'codigo_fase', 'titulo']
        # widgets = {
        #     'codigo_nivel': TextInput(),
        #     'codigo_fase' : TextInput(),
        #     }

    def clean_codigo_nivel(self):
        try:
            nivel = self.data['codigo_nivel']
            codigo_jogo = self.data['codigo_jogo']
            return NiveisJogo.objects.get(nivel=nivel, codigo_jogo=codigo_jogo)
        except:
            raise ValidationError(
                    ('Nivel invalido')
                )

    def clean_codigo_fase(self):
        try:
            fase = self.data['codigo_fase']
            codigo_jogo = self.data['codigo_jogo']
            return FasesJogo.objects.get(fase=fase, codigo_jogo=codigo_jogo)
        except:
            raise ValidationError(
                    ('Fase invalida')
                )
        
class FasesJogo_Form(Form_Bootstrap):
    class Meta:
        model = FasesJogo
        fields = ['fase','codigo_jogo','codigo_nivel','titulo']
        # widgets = {
        #     'codigo_nivel': TextInput(),
        #    }
        
    def clean_codigo_nivel(self):
        try:
            nivel = self.data['codigo_nivel']
            codigo_jogo = self.data['codigo_jogo']
            return NiveisJogo.objects.get(nivel=nivel, codigo_jogo=codigo_jogo)
        except:
            raise ValidationError(
                    ('Nivel invalido')
                )


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class UploadFileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })
    file = forms.FileField()