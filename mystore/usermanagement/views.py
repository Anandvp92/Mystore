from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm,LoginForm
# Create your views here.
from django.contrib.auth import login,logout,authenticate
from .models import CustomUserModel
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method=="POST":
        form=UserForm(request.POST,request.FILES)
        if form.is_valid():
            email = form.cleaned_data['emaireturn redirect("indexpage")l']
            phonenumber = form.cleaned_data['phonenumber']
            bio = form.cleaned_data['bio']
            profile_pic = form.cleaned_data['profile_pic']
            password = form.cleaned_data['password']
            new_user=CustomUserModel.objects.create(email=email,phonenumber=phonenumber,bio=bio,profile_pic=profile_pic,password=password)
            new_user.set_password(password)
            new_user.save()
            return HttpResponse(f"Created new user {email}") 

    else:
        form=UserForm()
        return render(request,"register.html",context={"userform":form})
        
    return render(request,"register.html",context={"userform":form})

def login_page(request):
    if request.POST:
        userform=LoginForm(request.POST)
        if userform.is_valid():
            emailid=userform.cleaned_data['email']
            password=userform.cleaned_data['password']
            user =  authenticate(email=emailid,password=password)
            if user is not None:
                login(request,user)
                return redirect("indexpage")
            else:
                return redirect('login_page')
    else:        
        userform=LoginForm()  

    return render(request,"login.html",{'loginform':userform})




@login_required
def index_page(request):
    return render(request,"index.html")