from django import forms
from .models import Blogdata

class Blogform(forms.ModelForm):
    class Meta:
        model = Blogdata
        fields = ['title', 'body']
