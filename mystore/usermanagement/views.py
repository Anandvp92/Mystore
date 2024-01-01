from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.

from .models import CustomUserModel



def register(request):
    if request.method=="POST":
        form=UserForm(request.POST,request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            bio = form.cleaned_data['bio']
            profile_pic = form.cleaned_data['profile_pic']
            password = form.cleaned_data['password']
            new_user=CustomUserModel.objects.create(email=email,phonenumber=phonenumber,bio=bio,profile_pic=profile_pic,password=password)
            new_user.set_password(password)
            new_user.save()
            return HttpResponse(f"Created new user {email}") 

        else:
            return render(request,'register.html',context={"userform":form})
    return render(request,"register.html",context={"userform":UserForm})
