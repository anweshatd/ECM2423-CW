from django import forms
from .models import Image
from challenges.models import Image
from django.forms import TextInput, FileInput

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ['title', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image title', 'style': 'width: 250px;'}),
            'image': FileInput(attrs={'class': 'form-control-file'})
        }
