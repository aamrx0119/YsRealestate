from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('',views.Home_view,name='f-main'),
]
