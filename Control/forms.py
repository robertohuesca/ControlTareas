from .models import Observacion
from django import forms
from django.forms import ModelForm

class Observacion_Form(forms.ModelForm):

    class Meta:
        model = Observacion
        exclude = ['']

    def clean(self):
        return self.cleaned_data