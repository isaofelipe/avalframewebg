"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from app.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class UploadFileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })
    file = forms.FileField()