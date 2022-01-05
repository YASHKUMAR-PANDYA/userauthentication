"""userauthentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userauth.views import register, userlogout
from userauth.views import userlogin
from userauth.views import home
from userauth.views import userlogout



urlpatterns = [
    path('admin/', admin.site.urls),

    #my urls
    path('', register, name='register'),
    path('userlogin/', userlogin, name='userlogin'),
    path('home/', home, name='home'),
    path('userlogout/', userlogout, name='userlogout'),


]
