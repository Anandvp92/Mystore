from typing import Any
from django.forms import ModelForm
from django import forms

from .models import CustomUserModel
class UserForm(ModelForm):    
    password=forms.CharField(label="Password",widget=(forms.PasswordInput(attrs={"placeholder":"Password"})))
    email=forms.EmailField(label="Email",widget=(forms.TextInput(attrs={"placeholder":"Email Id"})))
    phonenumber=forms.CharField(label="Phone Number",max_length=10,min_length=1,widget=forms.TextInput(attrs={"placeholder": "Phone Number"}))
    bio=forms.CharField(label="Bio",max_length=50,min_length=10,widget=forms.TextInput(attrs={"placeholder":"Bio"}))

    class Meta:       
        model=CustomUserModel
        fields=['email','phonenumber','bio','profile_pic','password']   

    def clean_phonenumber(self):
        phone_number = self.cleaned_data.get("phonenumber")
        
        if len(phone_number) != 10:
            raise forms.ValidationError("This is not a valid phone number!")
        
        elif CustomUserModel.objects.filter(phonenumber=phone_number).exists():
            raise forms.ValidationError("Already Taken!")        
        return phone_number
    

    
    
    def clean_email(self):
        Email = self.cleaned_data.get("email")
        if CustomUserModel.objects.filter(email=Email).exists():
            raise forms.ValidationError("Already Taken!")
        return Email
    


class LoginForm(forms.Form):    

    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={"placeholder":"Email Id"}))

    def clean_email(self):
        Email = self.cleaned_data.get("email")
        if not CustomUserModel.objects.filter(email=Email).exists():
            raise forms.ValidationError("User Not Found!")
        return Email    
    