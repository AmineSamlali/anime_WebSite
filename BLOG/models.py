from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
import random
import string
from  django.contrib.auth.models import User
from datetime import datetime
from io import BytesIO
from PIL import Image
from django.core.files import File
from profiles.models import Profile
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'PNG', quality=50) 
    new_image = File(im_io, name=image.name)
    return new_image

class blog(models.Model):
    '''
        Creating data base aboit 'index_anime_list ' 
    '''
    # start creating #
    ANM_title = models.CharField(max_length=290)
    ANM_sub_title = models.CharField(max_length=100)
    ANM_description = models.TextField(max_length=490)
    ANM_image = models.ImageField(upload_to='ANM_IMAGES/')
    ANM_Category =  models.ForeignKey("ANM_Category",on_delete=models.CASCADE)
    ANM_Type = models.ForeignKey("ANM_Type",on_delete=models.CASCADE)
    ANM_Studios = models.ForeignKey('ANM_Studios' , on_delete=models.CASCADE)
    ANM_Date_aired = models.DateTimeField(auto_now=False, auto_now_add=False)
    ANM_Status = models.ForeignKey("ANM_Status",on_delete=models.CASCADE)
    Genre = models.ManyToManyField('ANM_Genre')
    ANM_Scores = models.CharField(max_length=70)
    ANM_Rating = models.CharField(max_length=70)
    ANM_Duration = models.CharField(max_length=70)
    ANM_Quality = models.ForeignKey("ANM_Quality", on_delete=models.CASCADE)
    slug  = models.SlugField(blank=True , null= True)
    def save(self, *args, **kwargs):
            i = string.ascii_lowercase
            e = random.randrange(0,26)
            empty_list = []
            empty_list.append(i)
            self.slug = slugify(self.ANM_title) + '-'+ empty_list[0][e]
            new_compress_image = compress(self.ANM_image)
            self.ANM_image =new_compress_image
            super(blog ,self).save(*args, **kwargs)
    def __str__(self):
        return self.ANM_title
    
class ANM_Category(models.Model):
    category_title = models.CharField(max_length=90)
    date_time = models.DateTimeField (auto_now=True)
    slug  = models.SlugField(blank=True , null=True)
    def order_by(self):
        return ['-date_time']
    def save(self,*args, **kwargs):
        self.slug = slugify(self.category_title)
        return super(ANM_Category,self).save(*args, **kwargs)
    def __str__(self):
        return self.category_title


class comment_self_anime(models.Model):
    # PRF_profile_image = models.OneToOneField(Profile,on_delete=models.CASCADE)
    PRF_profile_image = models.ImageField()
    auther = models.ForeignKey(User,on_delete=models.CASCADE , blank=True, null=True)
    self_animee = models.ForeignKey('blog', on_delete=models.CASCADE)
    datetima = models.DateTimeField(auto_now=True)
    Comment = models.TextField(max_length = 450)
    def __str__(self):
        return self.Comment

class ANM_Type(models.Model):
    ANM_Type = models.CharField(max_length=100)
    def __str__(self):
        return self.ANM_Type

class ANM_Studios(models.Model):
    ANM_Studios = models.CharField(max_length=100)
    def __str__(self):
        return self.ANM_Studios

class ANM_Status(models.Model):
    ANM_Status = models.CharField(max_length=100)
    def __str__(self):
        return self.ANM_Status

class ANM_Genre(models.Model):
    ANM_Genre = models.CharField(max_length=100)
    def __str__(self):
        return self.ANM_Genre

class ANM_Quality(models.Model):
    ANM_Quality = models.CharField(max_length=80 )
    def __str__(self):
        return self.ANM_Quality





    