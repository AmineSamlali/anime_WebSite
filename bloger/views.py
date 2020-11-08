from django.shortcuts import render ,get_object_or_404 ,redirect
from django import http
from django.contrib import messages
from .models import DB_Bloger , Comment,ReplayToComment
def Home(request):
    DB_Blog = DB_Bloger.objects.all()
    context = {
        'blogs':DB_Blog,
    }
    return render(request,'blog/blog.html',context)
    
def Self_Blog(request , slug):
    f = Comment.objects.all().count()
    fixing = Comment.objects.all()
    replays = ReplayToComment.objects.all()
    self_blog = get_object_or_404(DB_Bloger ,slug=slug)
    ali = self_blog.Keyworda
    KeyWord_splitting  = ali.split(",")
    user_auth = request.user
    Comments = Comment.objects.filter(comment_self_Post=self_blog).order_by('-comment_date_time')
    if request.method =="POST":
        if 'Comment' in request.POST:
            content = request.POST['Comment']
            if len(content)  <= 0:
                messages.error(request , "Error You Cant Send Empty Data")
            else:
                comment = Comment.objects.create(comment_content=content,comment_auther=request.user , comment_self_Post=self_blog)
                comment.save()
        elif 'CommentReplay' in request.POST:
            server = request.POST['server_id']
            comment_content_ = request.POST['CommentReplay']
            com = Comment.objects.get(id=server)
            replay  = ReplayToComment.objects.create(auther=request.user , comment=com , comment_content=comment_content_)
            replay.save()
    context ={
        'blog':self_blog,
        'Comments':Comments,
        'COMMENT_COUNT':f,
        'replays':replays,
        'user_auth' :user_auth,
        'Keywords':KeyWord_splitting,
    }
    return render(request,'blog/blog-details.html',context)



def like_testing(request , id):
    like  = get_object_or_404(Comment,id = id)
    if request.user == like.comment_auther:
        return redirect(f'/blog/{like.comment_self_Post.slug}')
    else:
        like.comment_like += 1
        like.save()
    return redirect(f'/blog/{like.comment_self_Post.slug}')
    print(like.comment_like)
    print("Done +1 like")


    print("+1 like")
    return render(request,'blog/blog-details.html')




def CCounting(request , id):
    like  = get_object_or_404(ReplayToComment,id=id)
    if request.user == like.auther:
        return redirect(f'/blog/{like.comment.comment_self_Post.slug}')
        # print("MAT9tedrsh"*100)
    
    else:
        like.comment_likes += 1
        like.save()
    return redirect(f'/blog/{like.comment.comment_self_Post.slug}')
    print(like.comment_likes)
    print("Done +1 like")


    print("+1 like")
    return render(request,'blog/blog-details.html')