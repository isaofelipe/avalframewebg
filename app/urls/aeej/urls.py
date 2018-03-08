"""
Definition of urls for AvalFrameWeb.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views

import app.forms
import app.views
from app.views import aeej

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', aeej.index.as_view(), name='aeej_index'),
    url(r'^novo_alterar/$', aeej.novo_alterar.as_view(), name='aeej_novo'),
    url(r'^novo_alterar/(?P<codigo>\d+)$', aeej.novo_alterar.as_view(), name='aeej_alterar'),
    url(r'^deletar/(?P<codigo>\d+)$', aeej.deletar.as_view(), name='aeej_deletar'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
