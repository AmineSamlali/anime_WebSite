from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'PNG', quality=50) 
    new_image = File(im_io, name=image.name)
    return new_image

class Profile(models.Model):
    user = models.OneToOneField(User  , on_delete=models.CASCADE)
    PRF_profile_image = models.ImageField(default='Noimage.jpg',)
    PRF_phone = models.CharField( max_length=90 ,blank=True  , null=True)
    PRF_Location =  models.CharField(max_length=276,blank=True  , null=True)
    def __str__(self):
        return f"Profile : {self.user}"
    def save(self ,*args, **kwargs):
        new_image = compress(self.PRF_profile_image)
        self.PRF_profile_image  = new_image
        super(Profile , self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
