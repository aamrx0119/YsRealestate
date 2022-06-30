from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.House_model)
admin.site.register(models.Profile)
admin.site.register(models.images_house)
admin.site.register(models.Like_house)
admin.site.register(models.Category)
admin.site.register(models.ContactUS)