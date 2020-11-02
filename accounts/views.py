from django.shortcuts import render ,redirect
from django.http import HttpResponse
from  .forms import CreatigUseraccount
from django.contrib import messages
from django.contrib.auth import authenticate ,login
from django.contrib.auth import login as auth_login
from django.contrib import auth




def register(request):
    form   = CreatigUseraccount()
    if request.method == "POST":
        form  = CreatigUseraccount(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "Your account hase been registred :) ")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username ,password=password)
            user_login  = login(request,user)
            return redirect('home')
        else:
            messages.error(request , "Please Enter True Values !")
    else:
        form = CreatigUseraccount()
    context ={ 
        'form':form,
    }
    return render (request , "accounts/signup.html",context)    


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        print(username , password)
        user = authenticate(username=username , password=password)
        if user is not None:
            auth_login(request , user)
            return redirect('home')
        elif user is None:
            messages.error(request,"Password or UserName is incorrect")
    context ={
        "":""
    }
    return render(request , "accounts/login.html",context)


def logout(request):
    auth.logout(request)
    return render(request,'accounts/logout.html')