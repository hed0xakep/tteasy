from django import forms
from . import models


class AddMatchForm(forms.ModelForm):
    class Meta:
        model = models.MatchModel
        fields = ('p2', 'set1p1', 'set1p2', 'set2p1', 'set2p2', 'set3p1',
                    'set3p2', 'set4p1', 'set4p2', 'set5p1', 'set5p2', 'video')
