from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  



class UserForm(UserCreationForm):
    first_name = forms.CharField(label="firstname")
    last_name = forms.CharField(label="lastname")
    username = forms.CharField(label='username', min_length=5, max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput) 
    class meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  

    def last_name_clean(self):  
        last_name = self.cleaned_data['last_name'].lower()  
        new = User.objects.filter(last_name=last_name)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return last_name

    def first_name_clean(self):  
        first_name = self.cleaned_data['first_name'].lower()  
        new = User.objects.filter(first_name=first_name)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return first_name
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1'],
            # self.cleaned_data['first_name'],  
            # self.cleaned_data['last_name']
        )  
        return user  