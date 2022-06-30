from operator import truediv
from pyexpat import model
from statistics import mode
from django.utils import timezone
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
    email = models.EmailField(max_length=50,blank=True,null=True)
    picture = models.ImageField(upload_to='Profile/',default='Profile/default.jpg')
    profile_premission =models.CharField(choices=CHOICES_ACCESS,default='Basic',max_length=5)
    expire_time = models.DateTimeField(default=timezone.now)
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
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='home_cat',blank=True,null=True)
    picture1 = models.ImageField(upload_to='house/',null=True,blank=True,default='homedefualt.png')
    published =models.BooleanField(default=False)
    liked = models.ManyToManyField(Profile,blank=True,related_name='likes')
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
    



class Like_house (models.Model) :
    CHOICES_LIKE = (
        ('Like','Like'),
        ('Unlike','Unlike'),
    )
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='profile_like')
    home = models.ForeignKey(House_model,on_delete=models.CASCADE,related_name='house_like')
    situation = models.CharField(choices=CHOICES_LIKE,default='Unlike',max_length=6)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.user} {self.home}'
    



class Category (models.Model) :
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,null=True,blank=True)


    def __str__(self) :
        return self.name



class ContactUS (models.Model) :
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=20)
    pm = models.TextField(max_length=150)


    def __str__(self) :
        return f"{self.name} & {self.email}" 





