"""
Definition of urls for AvalFrameWeb.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views

import app.forms
import app.views
from app.views import aprendizagens_aeej

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', aprendizagens_aeej.index.as_view(), name='aprendizagens_aeej_index'),
    url(r'^novo_alterar/$', aprendizagens_aeej.novo_alterar.as_view(), name='aprendizagens_aeej_novo'),
    url(r'^novo_alterar/(?P<codigo>\d+)$', aprendizagens_aeej.novo_alterar.as_view(), name='aprendizagens_aeej_alterar'),
    url(r'^deletar/(?P<codigo>\d+)$', aprendizagens_aeej.deletar.as_view(), name='aprendizagens_aeej_deletar'),
    url(r'^novo_alterar/gerar_niveis$', aprendizagens_aeej.buscar_niveis, name='gerar_niveis'),
    url(r'^novo_alterar/gerar_fases$', aprendizagens_aeej.buscar_fases, name='gerar_fases'),
    url(r'^novo_alterar/gerar_etapas$', aprendizagens_aeej.buscar_fases, name='gerar_etapas'),
]
