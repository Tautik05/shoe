from django.db import models
from django.contrib.auth.models import User
# from django.db import AbstractUser
# from django.contrib.auth.base_user import BaseUserManager




# class UserManager(BaseUserManager):
    
#     def create_user(self , phone_number ,password = None , **extra_fields):

#         if not phone_number:
#             raise ValueError("Phone number is required")
        
#         extra_fields['email'] = self.normalize_email(extra_fields['email'])
#         user = self.model(phone_number = phone_number, **extra_fields)
#         user.set_password(password)
#         user.save(using = self.db)

#         return user



#     def create_superuser(self , phone_number , password = None, **extra_fields):
#         extra_fields.setdefault('is_superuser' , True)
#         extra_fields.setdefault('is_active' , True)

#         return self.create_user(phone_number, password, **extra_fields)







# # Create your models here.
# class Customuser(AbstractUser):
#     user_name=models.CharField(max_length=50)
#     phone_number=models.IntegerField(max_length=50,unique=True)
#     email=models.CharField(max_length=50,unique=True)
    

#     USERNAME_FIELD='phone_number'
#     REQUIRED_FIELD=[]

#     objects= UserManager()






class Consumer(models.Model):

    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True , blank=True)
    phone_number=models.IntegerField(unique=True)
    email=models.EmailField(max_length=50, unique=True)
    

