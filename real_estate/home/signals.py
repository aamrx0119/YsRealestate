from django.contrib.auth.models import User
from django.db.models.signals import post_save ,pre_delete , pre_save
from .models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def Create_profile(sender,instance,created,**kwargs):
    if created :
        inst = instance
        user = User.objects.get(username=inst.username)
        Profile.objects.create(user=user,first_name=inst.username,)


        

@receiver(pre_delete, sender=User)
def Delete_profile(sender,instance,**kwargs):
    inst = instance.username
    user = User.objects.get(username=inst)
    profile = Profile.objects.get(user=user)
    profile.delete()






    

