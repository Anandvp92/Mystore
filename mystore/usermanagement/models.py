from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin



# Create your models here.


#Custom User Manager 

class CustomUserManager(BaseUserManager):

    def create_user(self, email,phonenumber, password=None, **extra_fields) -> Any:
        if not email:
            raise ValueError("Email is required!")
        if not phonenumber:
            raise ValueError("Phone number is required!")       
        email= self.normalize_email(email)
        user= self.model(email=email,phonenumber=phonenumber,**extra_fields)
        user.set_password(password)
        user.is_active=True
        user.is_staff=True
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email,phonenumber,password=None, **extra_fields):
        # Ensure to include phone_number when calling create_user
        user = self.create_user(email=email,phonenumber=phonenumber,password=password, **extra_fields)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    
# Custom User Model 

class CustomUserModel(AbstractBaseUser,PermissionsMixin):
    email=models.CharField(verbose_name="Email",max_length=40,unique=True)
    phonenumber=models.CharField(verbose_name="Phone Number",max_length=13,unique=True)
    bio=models.CharField(verbose_name="Bio",max_length=40,blank=True)
    profile_pic = models.ImageField(verbose_name="Profile Pic",upload_to="profilepic/",null=True,blank=True)
    last_login=models.DateField(verbose_name="last login",default=timezone.now)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phonenumber']


    objects=CustomUserManager()


    def __str__(self):
      return  self.email



