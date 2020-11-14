from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import ProfileForm ,UserForm , PasswordChangeForm_F
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from BLOG.models import comment_self_anime
from bloger.models import Comment , ReplayToComment
from BLOG.models import ANM_Category
from django.contrib.auth import update_session_auth_hash


def profile(request):
    categorys = ANM_Category.objects.all()
    comments_count = comment_self_anime.objects.filter(auther=request.user).count()
    Comment_blog_count = Comment.objects.filter(comment_auther=request.user).count()
    Comment_likes_count = Comment.objects.filter(comment_auther=request.user)
    ReplayToComment_count = ReplayToComment.objects.filter(auther=request.user).count()
    ReplayToComment_likes = ReplayToComment.objects.filter(auther=request.user)
    comments_count += Comment_blog_count
    comments_count += ReplayToComment_count
    my_like_count = 0
    for coeemment in Comment_likes_count:
        my_like_count += coeemment.comment_like 

    for likes  in ReplayToComment_likes:
        my_like_count += likes.comment_likes 
    global_change  = my_like_count 
    #########################################################
    profilee = Profile.objects.get(user=request.user)
    Profiles = ProfileForm()
    UserForme = UserForm()
    if request.method == "POST":
        if 'FORMM1' in request.POST:
            Profiles = ProfileForm(request.POST,request.FILES,instance=profilee)
            UserFineal = UserForm(request.POST,instance=request.user)
            if Profiles.is_valid() or UserFineal.is_valid():
                UserFineal.save()   
                my_form = Profiles.save(commit=False)
                my_form.user = request.user
                my_form.save()
                messages.success(request , 'Your changes have been saved successfully')


    else:
        UserForme = UserForm(instance=request.user)
        Profiles = ProfileForm(instance=profilee)

    context = {
        'Profile':Profiles ,
        'profilee':profilee, 
        'User':UserForme , 
        'categorys':categorys,
        'my_like_count':my_like_count,
        'comments_count':comments_count,
        'profilee.PRF_phone':profilee.PRF_phone,
        'profilee.PRF_Location':profilee.PRF_Location,
        'user_new':request.user,
    }
    return render(request , 'profile/pp.html' , context)




def change_password(request):
    categorys = ANM_Category.objects.all()
    comments_count = comment_self_anime.objects.filter(auther=request.user).count()
    Comment_blog_count = Comment.objects.filter(comment_auther=request.user).count()
    Comment_likes_count = Comment.objects.filter(comment_auther=request.user)
    ReplayToComment_count = ReplayToComment.objects.filter(auther=request.user).count()
    ReplayToComment_likes = ReplayToComment.objects.filter(auther=request.user)
    comments_count += Comment_blog_count
    comments_count += ReplayToComment_count
    my_like_count = 0
    for coeemment in Comment_likes_count:
        my_like_count += coeemment.comment_like 

    for likes  in ReplayToComment_likes:
        my_like_count += likes.comment_likes 
    global_change  = my_like_count 

    profilee = Profile.objects.get(user=request.user)
    form = PasswordChangeForm_F(request.user)
    if request.method == "POST":
        form = PasswordChangeForm_F(request.user , request.POST)
        if form.is_valid():
            form = form.save()
            update_session_auth_hash(request  , form)
            messages.success(request ,  'Your Password Has been changed !')
            return redirect('/')
        else:
            print("NUP")
    else:
        form = PasswordChangeForm_F(request.user)

    context ={ 
        'profilee':profilee, 
        'user_new':request.user,
        'form':form,
        'profilee':profilee, 
        'categorys':categorys,
        'my_like_count':my_like_count,
        'comments_count':comments_count,
        'profilee.PRF_phone':profilee.PRF_phone,
        'profilee.PRF_Location':profilee.PRF_Location,
        'user_new':request.user,

    }
    return render(request , 'profile/change_password.html' , context )