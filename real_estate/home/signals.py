from django.contrib.auth.models import User
from django.db.models.signals import post_save ,pre_delete , pre_save
from .models import Profile , Like_house, House_model
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

@receiver(post_save, sender=Like_house)
def Create_profile(sender,instance,created,**kwargs):
    if created :
        inst_p = instance.user
        inst_h = instance.home
        house = House_model.objects.get(id=inst_h.id)
        house.liked.add(inst_p)
        house.save()



@receiver(pre_delete, sender=Like_house)
def Delete_profile(sender,instance,**kwargs):
    home = instance.home
    profile = instance.user
    house  = House_model.objects.get(id=home.id)
    house.liked.remove(profile)






    

