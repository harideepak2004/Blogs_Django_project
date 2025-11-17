from django import forms
from .models import Blog   # Import the Blog model

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog  
        fields = ['title', 'details', 'author']
