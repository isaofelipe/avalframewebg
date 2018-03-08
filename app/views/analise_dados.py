from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from django.views.generic.base import View
from datetime import datetime
from app.forms import *
from app.models import *

class index(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'analise_dados/index.html',
            {
                
            }
        )
    '''
    def post(self, request, *args, **kwargs):
        entrada = kwargs.get('entrada', None)
    '''