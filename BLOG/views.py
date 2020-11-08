from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse
from .models import blog,comment_self_anime,ANM_Category
from django.contrib import messages
from datetime import datetime
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
import string
def Home(request):
    blogs  = blog.objects.all()
    self_anime_2 = comment_self_anime.objects.filter()
    categorys = ANM_Category.objects.all()
    context = {
        'Blogs':blogs,
        'categorys':categorys,
        'self_anime_2':self_anime_2,
    }
    return render(request , 'home\index.html',context)

def details(request , slug):
    profille = Profile.objects.get(user=request.user)
    self_anime = get_object_or_404(blog , slug=slug)
    self_anime_2 = blog.objects.get(slug=slug)
    categorys = ANM_Category.objects.all()
    forming = CommentForm
    auto = request.user
    print(auto)

    if request.method == "POST":
        amine   = request.POST['commentsec']
        if len(amine) == 0:
            messages.error(request , "sorry you can't send empty data")
        else:
            Comment  = comment_self_anime.objects.create(PRF_profile_image=profille.PRF_profile_image , auther=request.user,Comment=amine ,self_animee=self_anime_2,datetima = datetime.now().hour)
            Comment.save()
    
    comments = comment_self_anime.objects.filter(self_animee=self_anime_2).order_by('-datetima')
    
    comment_count = comments.count()
    

    context ={
        'comment_count':comment_count,
        'anime': self_anime,
        'categorys':categorys,
        'forming':forming,
        'auto':auto,
        'comments':comments,
        'date_time':datetime.now().hour
    }
    return render(request , 'home/anime-details.html',context)


def get_category(request , id):
    blogs = blog.objects.filter(ANM_Category_id=id)
    categorys = ANM_Category.objects.all()
    naming = ANM_Category.objects.get(id=id)
    context = {
        'slef_glogs':blogs,
        'naming':naming,
        'categorys':categorys,
    }
    return render(request ,  'home/category.html' ,context)

@login_required
def edite(request , id):
    The_coment = comment_self_anime.objects.get(id=id)
    if request.user == The_coment.auther:
        if request.method =="POST":
            comment = request.POST['commentsec']
            The_coment.Comment = comment
            The_coment.save()
            return redirect(f'/{The_coment.self_animee.slug}')
        context = {
                'The_coment':The_coment,
            }

    else:
        return redirect('login')
    return render(request , 'home/edite.html',context)
@login_required
def deleting(request , id):
    the_ccont = comment_self_anime.objects.get(pk=id)
    if request.user == the_ccont.auther:
        the_ccont.delete()
    else:
        return redirect(f'/{the_ccont.self_animee.slug}')
    return redirect(f'/{the_ccont.self_animee.slug}')
    return render(request , 'home/anime-details.html')




