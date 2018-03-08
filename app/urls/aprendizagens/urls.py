"""
Definition of urls for AvalFrameWeb.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views

import app.forms
import app.views
from app.views import aprendizagens

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', aprendizagens.index.as_view(), name='aprendizagens_index'),
    url(r'^novo_alterar/$', aprendizagens.novo_alterar.as_view(), name='aprendizagens_novo'),
    url(r'^novo_alterar/(?P<codigo>\d+)$', aprendizagens.novo_alterar.as_view(), name='aprendizagens_alterar'),
    url(r'^deletar/(?P<codigo>\d+)$', aprendizagens.deletar.as_view(), name='aprendizagens_deletar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
