import re
from django.shortcuts import render

def Home_view(request):
    return render(request,'home/index.html')