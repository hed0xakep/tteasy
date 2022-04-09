from django import forms
from . import models

class PostCreateForm(forms.Form):
    class Meta:
        model = models.PostModel
        fields = ('title', 'description', 'city', 'delete_date')
