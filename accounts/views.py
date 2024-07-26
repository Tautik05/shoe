from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login

# Create your views here.




def register_page(request):
    
    if request.method == "POST":
        username = request.POST.get('user_name')
        phone_number=request.POST.get('phone_number')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')



        phone = Consumer.objects.filter(phone_number=phone_number)

        
        emailid = Consumer.objects.filter(email=email_id)

        if phone.exists() and emailid.exists():
            messages.info(request, 'user has an account')
            return redirect('/register')
    
        try:
           user = User.objects.get(username=username)
           messages.error(request, 'Username already taken.')
           return redirect('/register')

        except User.DoesNotExist:
          user = User.objects.create(username=username)
          user.set_password(password)
          user.save()


    

        Consumer.objects.create(
        user = user,
        phone_number = phone_number,
        email = email_id
        )


        messages.success(request, 'Account created successfully')
        return redirect('shoe')
   
    return render(request, 'register.html')
    



# def login_page(request):
#     if request.method =="POST":
#         username = request.POST.get('username')
#         phone_number = request.POST.get('phone_number')
#         email = request.POST.get('email_id')
#         password = request.POST.get('password')

#         try:
#             consumer = Consumer.objects.get(phone_number=phone_number, email=email)
#         except Consumer.DoesNotExist:
#             messages.info(request, 'User does not exist. Please create an account.')
#             return redirect('/register')
        
#         user = consumer.user  
#         if user is not None and user.check_password(password):
#           login(request, user)
#           messages.success(request, 'Login successful!')
#           return redirect('/home')
#     else:
#         messages.error(request, 'Invalid credentials. Please try again.')
#         return redirect('/login')

#     return render(request, 'login.html')
        



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email_id')
        password = request.POST.get('password')

        try:
            consumer = Consumer.objects.get(phone_number=phone_number, email=email)
        except Consumer.DoesNotExist:
            messages.info(request, 'User does not exist. Please create an account.')
            return redirect('/register')
        
        user = consumer.user  
        if user is not None and user.check_password(password):
            request.session["consumer_id"]=consumer.id
            login(request, user)
            messages.success(request, 'Login successful!')

            return redirect('shoe')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('/login')
    
    return render(request, 'login.html')





def logout_page(request):
   if 'consumer_id' in request.session:
       del request.session['consumer_id']
   logout(request)
   return redirect('shoe')

