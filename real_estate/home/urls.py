from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('',views.Home_view,name='f-main'),
    # path('<str:status>/',views.Home_view,name='contact-main'),
    path('homes/',views.Homes,name='homes'),
    path('home/<int:id>',views.Detail_home,name='detail_home'),
    path('home/like/',views.Like_Home,name='like_home'),
    # path('contact-us',views.ContactView,name='view_contact'),
]
