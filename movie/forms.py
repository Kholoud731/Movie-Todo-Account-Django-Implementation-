from django import forms
from django.forms import fields
from .models import Movie


class AddForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = '__all__'