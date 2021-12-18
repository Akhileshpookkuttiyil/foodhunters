from django import forms
from .models import Vlog


class ModelForm(forms.ModelForm):
    class Meta:
        model = Vlog
        fields = ['title','date','location','image','description','author']
