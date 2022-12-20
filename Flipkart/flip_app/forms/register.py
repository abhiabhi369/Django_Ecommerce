from django import forms
from django.forms import ModelForm

from flip_app.models import Users

class RegisterForm(ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False))
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    # email = forms.EmailField(unique=True,error_messages={'unique':'This emial address is alredy exist with us, please try with othe email'})
    class Meta:
        model = Users
        fields = '__all__'
        exclude = ('token',)
        error_messages = {
            'address': {
                u'unique': ('That address has already been added.'),
            }
        }


class LoginForm(forms.Form):
    Username = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=10,widget=forms.PasswordInput)

