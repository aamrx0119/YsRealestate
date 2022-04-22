from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView ,ListAPIView , RetrieveAPIView
from .serializers import Home_Serializer , Profile_Serializer
from home.models import House_model , Profile
from .permissions import IsSuperUser , IsStaffOrReadOnly , IsSellerOrReadOnly , IsSuperUserOrStaffOnly
# Create your views here.

class HomesSerializerView(ListCreateAPIView) :
    queryset = House_model.objects.all()
    serializer_class = Home_Serializer
    permission_classes = (IsSuperUserOrStaffOnly,)
    


class DetailHomesSerializerView(RetrieveUpdateDestroyAPIView) :
    queryset = House_model.objects.all()
    serializer_class = Home_Serializer
    permission_classes = (IsStaffOrReadOnly,IsSellerOrReadOnly)


class ProfileSerializerView (ListCreateAPIView) :
    queryset = Profile.objects.all()
    serializer_class = Profile_Serializer
    permission_classes = (IsSuperUser,)

class DetailProfileSerializerView (RetrieveAPIView) :
    queryset = Profile.objects.all()
    serializer_class = Profile_Serializer
    lookup_field = 'first_name'

