"""
Definition of urls for AvalFrameWeb.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views

import app.forms
import app.views
from app.views import jogos_digitais

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', jogos_digitais.index.as_view(), name='jogos_digitais_index'),
    url(r'^novo_alterar/$', jogos_digitais.novo_alterar.as_view(), name='jogos_digitais_novo'),
    url(r'^novo_alterar/(?P<codigo>\d+)$', jogos_digitais.novo_alterar.as_view(), name='jogos_digitais_alterar'),
    url(r'^deletar/(?P<codigo>\d+)$', jogos_digitais.deletar.as_view(), name='jogos_digitais_deletar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
