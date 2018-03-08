"""
Definition of urls for AvalFrameWeb.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf.urls import include

import app.forms
from app.views import home
from app.views import analise_dados

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^analise_dados/', include('app.urls.analise_dados.urls')),
    url(r'^$', home.home, name='home'),
    url(r'^competencias/', include('app.urls.competencias.urls')),
    url(r'^niveis_competencia_avaliacao/', include('app.urls.niveis_competencia_avaliacao.urls')),
    url(r'^aprendizagens/', include('app.urls.aprendizagens.urls')),
    url(r'^niveis_aprendizagem/', include('app.urls.niveis_aprendizagem.urls')),
    url(r'^jogos_digitais/', include('app.urls.jogos_digitais.urls')),
    url(r'^niveis_jogo/', include('app.urls.niveis_jogo.urls')),
    url(r'^aeej/', include('app.urls.aeej.urls')),
    url(r'^dispositivos_captura/', include('app.urls.dispositivos_captura.urls')),
    url(r'^jogadores/', include('app.urls.jogadores.urls')),
    url(r'^aprendizagens_aeej/', include('app.urls.aprendizagens_aeej.urls')),
    url(r'^competencias_aprendizagens/', include('app.urls.competencias_aprendizagens.urls')),
    url(r'^etapas_jogo/', include('app.urls.etapas_jogo.urls')),
    url(r'^fases_jogo/', include('app.urls.fases_jogo.urls')),
    
    
    url(r'^carga_aprendizagens/', include('app.urls.carga_aprendizagens.urls')),
    
    url(r'^geracao_relatorio/', include('app.urls.geracao_relatorio.urls')),
    
    

    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title': 'Log in',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
