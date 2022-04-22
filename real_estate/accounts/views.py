from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from home.models import Profile , House_model , images_house
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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
                messages.success(request,'You signup to our website please Login now','info')
                form = forms.Sign_up()
                return redirect('accounts:login_view')
                
    else:
        form = forms.Sign_up()

    context = {
        'form' :form,
        
    }

    return render(request,'accounts/signup.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login_Acc (request) :
    next_url = request.GET.get('next')
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
                # messages.success(request,'Log in successfully','success')
                login(request,user)
                if next_url:
                    return redirect(next_url)
                return redirect('accounts:dashboard_view',user.id)
            else :
                messages.error(request,"Your password or username doesn't match",'danger')
                form = forms.Log_in()               
    else :
        form = forms.Log_in()
    context = {
        'form' :form,
        
    }
    
    return render (request,'accounts/login.html',context)


def Logout_Acc (request):
    logout(request)
    return redirect('home:f-main')

@login_required
def Dashboard_Acc(request,id):
    user = User.objects.get(pk=id)
    profile = Profile.objects.get(user=user)
    Adv = Profile.objects.Get_Profile_Ad(profile=profile)


    if request.user != user :
        return redirect ('accounts:login_view')




    context = {
        'profile':profile,
        'Adv':Adv,
    }
    return render (request,'accounts/dashboard.html',context)

    
def Form_page(request,id):
    user = User.objects.get(pk=id)
    profile = Profile.objects.get(user=user)

    if request.user != user :
        return redirect ('accounts:login_view')

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

            subject = 'Add an advertiser'
            message = f'Hello sir a user who is {user.username} send a request to add an advertiser'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ('ali.bk0010@gmail.com',)
            send_mail( subject, message, email_from, recipient_list )
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

@login_required
def Change_profile_view (request,id) :

    user = User.objects.get(pk=id)
    profile = Profile.objects.get(user=user)

    if request.user != user :
        logout(request)
        return redirect ('accounts:login_view')

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





class Password_Reset_view (auth_views.PasswordResetView):
    template_name = 'accounts/reset/password_reset_form.html'
    success_url =  reverse_lazy ('accounts:password_reset_done')
    html_email_template_name = 'accounts/reset/password_reset_email.html'
    form_class = forms.Email_Forget_Form
    


class Password_Reset_Done (auth_views.PasswordResetDoneView):
    template_name = 'accounts/reset/password_reset_done.html'


class Password_Reset_Confirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/reset/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    form_class = forms.Email_Changepassword_Form
    

class Password_Reset_Complete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/reset/password_reset_complete.html'


   
    
    
