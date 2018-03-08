# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.utils.encoding import force_text
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
    valor_maximo = models.IntegerField(blank=True, null=True)

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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BaseConsolidada(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_jogador = models.IntegerField(blank=True, null=True)
    data_inicio_jogo = models.DateField(blank=True, null=True)
    hora_inicio_jogo = models.TimeField(blank=True, null=True)
    codigo_jogo = models.IntegerField(blank=True, null=True)
    codigo_aprendizagem = models.IntegerField(blank=True, null=True)
    valor_aprendizagem = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_consolidada'


class Competencias(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(unique=True, max_length=30)
    valor_maximo_pontos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competencias'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class HistoricoRegistro(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_jogador = models.IntegerField(blank=True, null=True)
    data_inicio_jogo = models.DateField(blank=True, null=True)
    hora_inicio_jogo = models.TimeField(blank=True, null=True)
    codigo_jogo = models.IntegerField(blank=True, null=True)
    nivel_jogo = models.IntegerField(blank=True, null=True)
    fase_jogo = models.IntegerField(blank=True, null=True)
    etapa_jogo = models.IntegerField(blank=True, null=True)
    tipo_aeej = models.CharField(max_length=1, blank=True, null=True)
    codigo_aeej = models.IntegerField(blank=True, null=True)
    valor1 = models.IntegerField(blank=True, null=True)
    valor2 = models.IntegerField(blank=True, null=True)
    valor3 = models.IntegerField(blank=True, null=True)
    data_gravacao = models.DateField(blank=True, null=True)
    hora_gravacao = models.TimeField(blank=True, null=True)
    nome_arquivo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_registro'


class Jogadores(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_desde_quando_joga = models.DateField(blank=True, null=True)
    coeficiente_de_rendimento = models.FloatField(blank=True, null=True)
    tipo_jogo_preferido = models.IntegerField(blank=True, null=True)
    perfil_recomendacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jogadores'


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
        return '%s - %s' % (self.nivel, force_text(self.titulo))
        
class ViewAlunoAprendizagem(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_jogador = models.CharField(max_length=30)
    titulo_aprendizagem = models.CharField(max_length=30)
    data_inicio_jogo = models.DateField()
    hora_inicio_jogo = models.TimeField()
    valor_aprendizagem = models.FloatField()
    titulo_nivel_aprendizagem = models.CharField(max_length=20)
    
    class Meta:
        managed = False
        db_table = 'vw_aluno_aprendizagem'