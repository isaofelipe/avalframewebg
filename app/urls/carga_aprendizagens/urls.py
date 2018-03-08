"""
Definition of urls for AvalFrameWeb.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
import django.contrib.auth.views

import app.forms
import app.views
from app.views import carga_aprendizagens

urlpatterns = [
    url(r'^$', carga_aprendizagens.index.as_view(), name='carga_aprendizagens_index'),
]