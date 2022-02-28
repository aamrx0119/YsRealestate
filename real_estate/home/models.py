from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    picture = models.ImageField(upload_to='Profile/',default='Profile/default.jpg')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return str(self.user)


    

class House_model (models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='p_house')
    name = models.CharField(max_length=50)
    information = models.TextField(max_length=500)
    compony = models.CharField(max_length=70,null=True,blank=True)
    picture1 = models.ImageField(upload_to='house/',null=True,blank=True)
    picture2 = models.ImageField(upload_to='house/',null=True,blank=True)
    picture3 = models.ImageField(upload_to='house/',null=True,blank=True)
    picture4 = models.ImageField(upload_to='house/',null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
