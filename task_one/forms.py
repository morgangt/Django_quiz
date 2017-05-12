from django import forms
from .models import Transportation


class NewTransForm(forms.ModelForm):
    class Meta:
        model = Transportation
        fields = ('model', 'cat',)
