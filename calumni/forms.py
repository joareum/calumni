from django import forms
from .models import Cal

class BlogPost(forms.ModelForm):
    class Meta:
        model = Cal
        fields = ['title','score','body']