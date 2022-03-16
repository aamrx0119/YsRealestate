from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('',views.Home_view,name='f-main'),
    path('homes/',views.Homes,name='homes'),
    path('home/<int:id>',views.Detail_home,name='detail_home'),
]
