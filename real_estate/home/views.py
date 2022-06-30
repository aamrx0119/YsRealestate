from . import models
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import forms
from django.contrib import messages

def Home_view(request):
    # print('*'*25)
    # client_ip = request.META['REMOTE_ADDR']
    # print(client_ip)
    if request.method == 'POST':
        form = forms.ContactUSForm(request.POST)
        if form.is_valid():
            messages.success(request,'Your message is sent','success')
            form.save()  
            form = forms.ContactUSForm()
        else:
            messages.error(request,'Somethong is wrong','warning')
            form = forms.ContactUSForm()
    else :
        form = forms.ContactUSForm()

    cat = models.Category.objects.all()

    context = {
        'cat':cat,
        'form':form,
    }
    return render(request,'home/index.html',context=context)


def Homes (request):
    exist = False
    if request.user.is_authenticated:
        user = request.user
        profile = models.Profile.objects.get(user=user)
        exist = True
    else:
        profile = None
    houses_q = models.House_model.objects.all()
    page = request.GET.get('page',1)
    
    
    paginator = Paginator(houses_q,6)
    try:
        houses = paginator.page(page)
    except PageNotAnInteger:
        houses = paginator.page(1)
    except EmptyPage:
        houses = paginator.page(paginator.num_pages)


    context = {
        'houses':houses,
        'exist':exist,
        'profile':profile,
    }
    return render (request,'home/homes.html',context)



def Detail_home (request,id) :
    house = models.House_model.objects.get(pk=id)

    context = {
        'house':house,
    }
    return render (request,'home/detail_house.html',context)


def Like_Home (request):
    if request.method == 'POST':
        house_id = request.POST.get('house_id')
        profile = models.Profile.objects.get(user = request.user)
        home = models.House_model.objects.get(id = house_id)
        like,created = models.Like_house.objects.get_or_create(user=profile,home=home)

        if not created :
            if like.situation == 'Like':
                like.situation = 'Unlike'
                home.liked.remove(profile)
                
            else:
                like.situation = 'Like'
                home.liked.add(profile)
        else:
            like.situation = 'Like'
            home.liked.add(profile)

        like.save()
    return redirect('home:homes')

# def ContactView (request) :
 

#     return redirect ('home:contact-main',status)

# Errors Views
def Error_404 (request,exception) :
    return render (request,'home/error/404.html')

def Error_505 (request,exception) :
    return render (request,'home/error/505.html')



        