# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Aeej(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_dispositivo = models.ForeignKey('DispositivosCaptura', models.DO_NOTHING, db_column='codigo_dispositivo')
    tipo = models.CharField(max_length=1, blank=True, null=True)
    descricao = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'aeej'

    def __str__(self):
        return '%s - %s' % (self.codigo, self.descricao)

class Aprendizagens(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1)
    titulo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'aprendizagens'
    
    def __str__(self):
        return '%s - %s' % (self.codigo, self.titulo)
        
class AprendizagensAeej(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_aprendizagem = models.ForeignKey(Aprendizagens, models.DO_NOTHING, db_column='codigo_aprendizagem')
    codigo_jogo = models.ForeignKey('JogosDigitais', models.DO_NOTHING, db_column='codigo_jogo')
    nivel_jogo = models.ForeignKey('NiveisJogo', models.DO_NOTHING, db_column='nivel_jogo')
    fase_jogo = models.ForeignKey('FasesJogo', models.DO_NOTHING, db_column='fase_jogo')
    etapa_jogo = models.ForeignKey('EtapasJogo', models.DO_NOTHING, db_column='etapa_jogo')
    codigo_aeej = models.ForeignKey(Aeej, models.DO_NOTHING, db_column='codigo_aeej')
    tipo_operacao = models.CharField(max_length=1)
    descritor_operacao = models.CharField(max_length=30, blank=True, null=True)
    valor_padrao = models.IntegerField()
    contribuicao_do_aeej_na_aprendizagem = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aprendizagens_aeej'
        unique_together = (('codigo_aprendizagem', 'codigo_jogo', 'nivel_jogo', 'fase_jogo', 'etapa_jogo', 'codigo_aeej'),)
        
class Competencias(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(unique=True, max_length=30)
    valor_maximo_pontos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competencias'
        
    def __str__(self):
        return '%s - %s' % (self.codigo, self.titulo)


class CompetenciasAprendizagens(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_competencia = models.ForeignKey(Competencias, models.DO_NOTHING, db_column='codigo_competencia')
    codigo_aprendizagem = models.ForeignKey(Aprendizagens, models.DO_NOTHING, db_column='codigo_aprendizagem')
    contribuicao_da_aprendizagem_na_competencia = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competencias_aprendizagens'
        unique_together = (('codigo_competencia', 'codigo_aprendizagem'),)
    

class DispositivosCaptura(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'dispositivos_captura'

    def __str__(self):
        return '%s - %s' % (self.codigo, self.nome)

class EtapasJogo(models.Model):
    codigo = models.AutoField(primary_key=True)
    etapa = models.IntegerField()
    codigo_jogo = models.ForeignKey('JogosDigitais', models.DO_NOTHING, db_column='codigo_jogo')
    codigo_nivel = models.ForeignKey('NiveisJogo', models.DO_NOTHING, db_column='codigo_nivel')
    codigo_fase = models.ForeignKey('FasesJogo', models.DO_NOTHING, db_column='codigo_fase')
    titulo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etapas_jogo'
        unique_together = (('etapa', 'codigo_jogo', 'codigo_nivel', 'codigo_fase'),)
        
    def __str__(self):
        return '%s - %s' % (self.etapa, self.titulo)


class FasesJogo(models.Model):
    codigo = models.AutoField(primary_key=True)
    fase = models.IntegerField()
    codigo_jogo = models.ForeignKey('JogosDigitais', models.DO_NOTHING, db_column='codigo_jogo')
    codigo_nivel = models.ForeignKey('NiveisJogo', models.DO_NOTHING, db_column='codigo_nivel')
    titulo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fases_jogo'
        unique_together = (('fase', 'codigo_jogo', 'codigo_nivel'),)
        
    def __str__(self):
        return '%s - %s' % (self.fase, self.titulo)


class Jogadores(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_desde_quando_joga = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogadores'
    
    def __str__(self):
        return '%s - %s' % (self.codigo, self.nome)


class JogosDigitais(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'jogos_digitais'
        
    def __str__(self):
        return '%s - %s' % (self.codigo, self.titulo)


class NiveisAprendizagem(models.Model):
    codigo = models.AutoField(primary_key=True)
    nivel = models.IntegerField()
    codigo_aprendizagem = models.ForeignKey(Aprendizagens, models.DO_NOTHING, db_column='codigo_aprendizagem')
    titulo = models.CharField(max_length=20, blank=True, null=True)
    inicio_nivel = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    fim_nivel = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    jogadores_nesse_nivel = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'niveis_aprendizagem'
        unique_together = (('nivel', 'codigo_aprendizagem'),)
        
    def __str__(self):
        return '%s - %s' % (self.codigo, self.titulo)


class NiveisCompetenciaAvaliacao(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_competencia = models.ForeignKey(Competencias, models.DO_NOTHING, db_column='codigo_competencia', blank=True, null=True)
    titulo = models.CharField(max_length=20, blank=True, null=True)
    inicio_nivel = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    fim_nivel = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    jogadores_nesse_nivel = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'niveis_competencia_avaliacao'
        
    def __str__(self):
        return '%s - %s' % (self.codigo, self.titulo)


class NiveisJogo(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_jogo = models.ForeignKey(JogosDigitais, models.DO_NOTHING, db_column='codigo_jogo')
    nivel = models.IntegerField()
    titulo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'niveis_jogo'
        unique_together = (('codigo_jogo', 'nivel'),)
    
    def __str__(self):
        return '%s - %s' % (self.codigo, self.titulo)