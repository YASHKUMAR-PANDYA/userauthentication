from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login 

from .forms import UserForm
from django.contrib import messages


# Create your views here.

def register(request):
    context = {}
    

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Your account was created with us as ' + user)
            return redirect('userlogin')
            
    else:
        form = UserForm()

    context['form'] = form
    return render(request, 'register.html', context)

def userlogin(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request,"username or password is incorrect")

    return render(request, 'login.html', context)
            
def userlogout(request):
    logout(request)
    return redirect('userlogin')

def home(request):
    context = {}
    return render(request, 'home.html', context)

