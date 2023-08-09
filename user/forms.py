from django.contrib.auth.models import User
from django import forms


class CadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)