from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages

class Sign_up (forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=50 ,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=65)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=65)


    def clean_email (self) :
        cd = self.cleaned_data
        user = User.objects.filter(email=cd['email'])
        if user.exists():
            raise forms.ValidationError('this email was used')
        return cd['email']
        


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2




class Log_in (forms.Form) :
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=65)

