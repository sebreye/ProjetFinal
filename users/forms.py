from django import forms 
from .models import Users


class InscriptionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Users
        fields = ['username', 'password', 'email', 'avatar']