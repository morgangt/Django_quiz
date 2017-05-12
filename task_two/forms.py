from django import forms
from .models import Action_User


class Action_UserForm(forms.ModelForm):
    class Meta:
        model = Action_User
        fields = ('type_action',)
