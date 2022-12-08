from django.shortcuts import render,redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(req):
    return render(req,'index.html')

def home(req):
    return render(req,'home.html')

def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        fname = req.POST['first_name']
        lname = req.POST['last_name']
        email = req.POST['email']
        pass1 = req.POST['password1']
        pass2 = req.POST['password2']


        if User.objects.filter(username=username):
            messages.error(req,'Username already exists!!')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(req,'Email already registered, please use different email.')
            return redirect('signup')

        elif pass1!=pass2:
            messages.error(req,"Password and Confirm password doesn't match ")
            return redirect('signup')
        
        user = User.objects.create_user(username=username,email=email,password = pass1)
        user.is_active = True
        user.first_name=fname
        user.last_name=lname
        user.save()

        messages.success(req,"Your account is successfully created!!! Please check your email to confirm your email address in order to activate your account.")

        return redirect('signin')

    else:
        return render(req,'signup.html')

def signin(req):
    print("inside")
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print("user vp:{}".format(user))
        if user is not None:
            print("no error")
            login(req, user)
            fname=user.first_name
            return render(req,"home.html")
        else:
            print("error to sigin ")
            messages.error(req, "Bad Credentials!!")
            return redirect('index')

    return render(req,"signin.html")


def signout(req):
    logout(req)
    messages.success(req,'Logout sucessfully')
    return redirect('index')

