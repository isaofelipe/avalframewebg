"""
Definition of urls for AvalFrameWeb.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views

import app.forms
import app.views
from app.views import fases_jogo

urlpatterns = [
    url(r'^$', fases_jogo.index.as_view(), name='fases_jogo_index'),
    url(r'^novo_alterar/$', fases_jogo.novo_alterar.as_view(), name='fases_jogo_novo'),
    url(r'^novo_alterar/(?P<codigo>\d+)$', fases_jogo.novo_alterar.as_view(), name='fases_jogo_alterar'),
    url(r'^deletar/(?P<codigo>\d+)$', fases_jogo.deletar.as_view(), name='fases_jogo_deletar'),
    url(r'^novo_alterar/gerar_niveis$', fases_jogo.buscar_niveis, name='gerar_niveis'),
]
