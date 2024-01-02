from django.forms import ModelForm
from django import forms

from .models import CustomUserModel
class UserForm(ModelForm):    
    password=forms.CharField(label="Password",widget=(forms.PasswordInput()))
    email=forms.EmailField(label="Email")
    phonenumber=forms.CharField(label="Phone Number",max_length=10,min_length=1)
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