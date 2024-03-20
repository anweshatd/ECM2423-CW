from django import forms
from .models import Image

from challenges.models import Image

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ['title', 'image']