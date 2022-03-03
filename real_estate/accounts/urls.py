from . import views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.Signup_Acc,name='signup_view'),
    path('login/',views.Login_Acc,name='login_view'),
]
