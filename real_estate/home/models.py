from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.



class Profile_manager(models.Manager):

    def Get_Profile_Ad(self,profile):
        Ad_qs = House_model.objects.filter(profile=profile) 
        return Ad_qs




class Profile(models.Model):

    CHOICES_ACCESS =(
        ('Gold','Gold'),
        ('Basic','Basic'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    picture = models.ImageField(upload_to='Profile/',default='Profile/default.jpg')
    profile_premission =models.CharField(choices=CHOICES_ACCESS,default='Basic',max_length=5)
    expire_time = models.DateTimeField(blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = Profile_manager()

    def __str__(self) :
        return str(self.user)


    

class House_model (models.Model):

    STATUS_CHOICES =(
        ('accept','accept'),
        ('reject','reject'),
        ('wait','wait'),
    )
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='p_house')
    name = models.CharField(max_length=50)
    information = models.TextField(max_length=500)
    compony = models.CharField(max_length=70,null=True,blank=True)
    picture1 = models.ImageField(upload_to='house/',null=True,blank=True,default='homedefualt.png')
    published =models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES,max_length=6,default='wait')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.name} -- {self.id}'

class images_house (models.Model) :
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    house = models.ForeignKey(House_model,on_delete=models.CASCADE,related_name='house_image')
    image = models.ImageField(upload_to = 'houses/%Y/%m/%d')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    


