from django import forms
from register.models import RegisterUsers

class UserForm(forms.ModelForm):
    class Meta:
        model = RegisterUsers
        widgets = {
        'password': forms.PasswordInput(),
    }