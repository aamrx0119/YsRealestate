from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from home.models import Profile , House_model , images_house
from django.utils import timezone
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
                obj = User.objects.get(username=cd['username'])
                up_time = Profile.objects.get(user=obj)
                up_time.updated = timezone.now()
                up_time.save()
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


def Dashboard_Acc(request,id):
    user = User.objects.get(pk=id)
    profile = Profile.objects.get(user=user)
    Adv = Profile.objects.Get_Profile_Ad(profile=profile)



    context = {
        'profile':profile,
        'Adv':Adv,
    }
    return render (request,'accounts/dashboard.html',context)

    
def Form_page(request,id):
    user = User.objects.get(pk=id)
    profile = Profile.objects.get(user=user)

    if request.method =='POST':
        form = forms.House_Model_Form(request.POST,request.FILES)
        files_image = request.FILES.getlist('pict')
        thumbnail = request.FILES.get('thumbnail')
        if form.is_valid():
            cd = form.save(commit=False)
            cd.profile = profile
            cd.picture1 = thumbnail
            cd.save()
            house = House_model.objects.get(id=cd.id)
            for x in files_image :
                images_house.objects.create(profile=profile,house=house,image=x)
            form = forms.House_Model_Form()
        else:
            print('wrongggggggggggggggggggggggggggg')
    else:
        form = forms.House_Model_Form()


    context = {
        'profile':profile,
        'form':form,
        
    }
    return render (request,'accounts/basic_elements.html',context)

def Change_profile_view (request,id) :
    user = User.objects.get(pk=id)
    profile = Profile.objects.get(user=user)

    form = forms.Change_Profile(request.POST or None,request.FILES or None,instance=profile)

    if request.method == 'POST' :
        pict = request.FILES.get('pict')
        if form.is_valid():
            cd = form.save(commit=False)
            cd.picture = pict
            cd.save()

    context = {
        'profile':profile,
        'form':form,
        
        
    }
    return render (request,'accounts/Change_profile_view.html',context)

def Checking_houses (request) :
    if request.user.is_superuser :
        user = request.user
        profile = Profile.objects.get(user=user)
        houses = House_model.objects.filter(status='wait')
        houses_accept = House_model.objects.filter(status='accept')

    else:
        return redirect('accounts:login_view')

    context = {
            'profile':profile,
            'houses':houses,
            'houses_accept':houses_accept,
                
        }
    return render (request,'accounts/Chaking_houses.html',context)


def Manage_house (request,id) :
    if request.user.is_superuser :

        if request.method == 'POST' :
            if 'delete' in request.POST:
                House_model.objects.get(pk=id).delete()
            else:
                house = House_model.objects.get(pk=id)
                status = request.POST.get('status')
                house.status = status
                house.save()
        return redirect('accounts:chacking_house')

    else:
         return redirect('accounts:login_view')



   
    
    
