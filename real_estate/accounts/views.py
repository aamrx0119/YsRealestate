from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages

# Create your views here.


def Signup_Acc (request) :
    if request.method == 'POST':
        form = forms.Sign_up(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            check_user = User.objects.filter(username=cd['username'])
            if check_user.exists():
                messages.success(request,'This username was created please change it','warning')
                form = forms.Sign_up()
            else:
                user = User.objects.create_user(username=cd['username'],first_name=cd['first_name'],last_name=cd['last_name'],email=cd['email'],password=cd['password2'])
                user.save()
                messages.success(request,'Welcome to Mrx Real Estate ','info')
                form = forms.Sign_up()
    else:
        form = forms.Sign_up()

    context = {
        'form' :form,
        
    }

    return render(request,'accounts/signup.html',context)


def Login_Acc (request) :
    if request.method == 'POST' :
        form = forms.Log_in(request.POST)
        if form.is_valid () :
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None :
                login(request,user)
                messages.success(request,'Log in successfully','success')
                form = forms.Log_in()
                return redirect('home:f-main')
            else :
                messages.error(request,"Your password or username doesn't match",'danger')
                form = forms.Log_in()
                
    else :
        form = forms.Log_in()
    context = {
        'form' :form,
        
    }
    
    return render (request,'accounts/login.html',context)