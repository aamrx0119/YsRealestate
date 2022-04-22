from rest_framework import serializers
from home.models import House_model , Profile





class Home_Serializer(serializers.ModelSerializer):
    class Meta:
        model = House_model
        fields = ('__all__')


class Profile_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Profile
        fields = ('__all__')