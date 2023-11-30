from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth .models import User
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.

def login(req):
    
    if(req.method == "POST"):
        login_form  = LoginForm(req.POST)        
        if login_form.is_valid():
            user =login_form.cleaned_data
            if user is not None:
                auth_login(req,user)                
                return redirect("index")   
            else:
                return render(req  , "authentication/login.html",{"form":login_form})           
        else:
            return render(req  , "authentication/login.html",{"form":login_form})           
    login_form = LoginForm()
    return render(req  , "authentication/login.html",{"form":login_form})

def signup(req):
    if req.method =="POST":
        
        user_form = UserCreationForm(req.POST)
        
        if user_form.is_valid():
            
            user = User(username = user_form.cleaned_data["username"])
            user.set_password(user_form.cleaned_data["password1"])
            user.save()
            return redirect('login')
        else:
            return render(req  , "authentication/signup.html" ,{"form":user_form})        
        
        
    userform  = UserCreationForm()
    return render(req  , "authentication/signup.html" ,{"form":userform})

def logout(req):
    auth_logout(req)
    return redirect("login")
    # return render(req  , "authentication/landing")