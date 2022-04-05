from django import forms
from . import models

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Homepost
        fields = ['title', 'body', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'})
        }
