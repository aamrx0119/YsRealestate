from . import models
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Home_view(request):
    return render(request,'home/index.html')




def Homes (request) :
    houses_q = models.House_model.objects.all()
    page = request.GET.get('page',1)

    paginator = Paginator(houses_q, 3)
    try:
        houses = paginator.page(page)
    except PageNotAnInteger:
        houses = paginator.page(1)
    except EmptyPage:
        houses = paginator.page(paginator.num_pages)

    context = {
        'houses':houses,
    }
    return render (request,'home/homes.html',context)



def Detail_home (request,id) :
    house = models.House_model.objects.get(pk=id)

    context = {
        'house':house,
    }
    return render (request,'home/detail_house.html',context)