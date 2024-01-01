from django.forms import ModelForm
from django import forms

from .models import CustomUserModel
class UserForm(ModelForm):    
    password=forms.CharField(label="Phone Number",widget=(forms.PasswordInput()))
    email=forms.EmailField(label="Email")
    class Meta:       
        model=CustomUserModel
        fields=['email','phonenumber','bio','profile_pic','password']

    def cleaned_email(self):
        email=self.cleaned_data.get("email")
        bio=self.cleaned_data.get("bio")
        if CustomUserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("This email id is already taken")
        return bio
    

    def clean_phonenumber(self):
        phonenumber = self.cleaned_data.get("phonenumber")
        if CustomUserModel.objects.filter(phonenumber=phonenumber).exists():
            raise forms.ValidationError("This phones number is already taken")
        return phonenumber
