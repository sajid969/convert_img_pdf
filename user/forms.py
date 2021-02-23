from django import forms
from django.contrib.auth.models import User
from user.models import *

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')

class filefieldForm(forms.ModelForm):
    class Meta:
        model=filefield
        fields=['choosefile']
