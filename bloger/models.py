from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class DB_Bloger(models.Model):
    Blog_name = models.CharField(max_length=200)
    category = models.ForeignKey("BLOG.ANM_Category",  on_delete=models.CASCADE)
    date_time = models.DateField(auto_now=True)
    content = models.TextField(max_length=4000)
    images = models.ImageField(upload_to="BLOGER/")
    tags  =  models.ManyToManyField("DB_Tags")
    Keyworda = models.CharField(max_length=140)
    slug = models.SlugField(blank=True , null=True)
    def save(self,*args, **kwargs):
        self.slug = slugify(self.Blog_name)
        super(DB_Bloger,self).save(*args, **kwargs)
    def __str__(self):
        return self.Blog_name
    


class DB_Tags(models.Model):
    Tags  = models.CharField(max_length=100)
    def __str__(self):
        return self.Tags



class Comment(models.Model):
    comment_datetime = models.DateField(auto_now=True)
    comment_date_time = models.DateTimeField( auto_now=True )
    comment_content = models.TextField(max_length=700)
    comment_auther = models.ForeignKey(User , on_delete=models.CASCADE)
    comment_self_Post = models.ForeignKey(DB_Bloger , on_delete=models.CASCADE)
    comment_like = models.IntegerField(default=0)
    def __str__(self):
        return self.comment_content
    

class ReplayToComment(models.Model):
    date_time  = models.DateField(auto_now=True)
    auther = models.ForeignKey(User , on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,related_name='Commenting', on_delete=models.CASCADE)
    comment_content = models.CharField( max_length=1000)
    comment_likes = models.IntegerField(default=0)
    def __str__(self):
        return self.comment_content