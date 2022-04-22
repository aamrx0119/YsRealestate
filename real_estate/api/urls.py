from . import views
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('',views.HomesSerializerView.as_view(),name='f-serializer'),
    path('home/<int:pk>/',views.DetailHomesSerializerView.as_view(),name='d-serializer'),
    path('profile/',views.ProfileSerializerView.as_view(),name='p-serializer'),
    path('profile/<str:first_name>/',views.DetailProfileSerializerView.as_view(),name='pd-serializer'),
]
