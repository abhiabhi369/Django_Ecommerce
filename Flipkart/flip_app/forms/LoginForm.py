from django import forms

class LoginForm(forms.Form):
    Username = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=10,widget=forms.PasswordInput)