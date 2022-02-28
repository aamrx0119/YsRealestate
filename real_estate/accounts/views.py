from django.shortcuts import render
from . import forms
from django.contrib.auth.models import User

# Create your views here.


def Signup_Acc (request) :
    form = forms.Sign_up
    users = User.objects.all()

    return render(request,'accounts/signup.html',{form :'form',users :'users'})