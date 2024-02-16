from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

#how to print a text
def logout(request):
     auth.logout(request)
     return redirect('/')
def login(request):
     if request.method == 'POST':
          uname=request.POST["username"]
          pwd=request.POST["password"]
          user1=auth.authenticate(username=uname,password=pwd)
          if user1 is not None:
                    auth.login(request,user1)
                    return redirect('/')
          else:
               messages.info(request, "Invalid user")
               return redirect('login')

     return render(request,'login.html')
def registrations(request):
     if request.method == 'POST':
          uname=request.POST["username"]
          fname=request.POST["firstname"]
          sname = request.POST["secondname"]
          mail=request.POST["email"]
          pwd=request.POST["password"]
          cpswd=request.POST["confirmpaswword"]
          if pwd==cpswd:
               if User.objects.filter(username=uname).exists():
                    messages.info(request,"User already exists")
                    return redirect('registrations')
               elif User.objects.filter(email=mail).exists():
                    messages.info(request,"Email id already exists")
                    return redirect('registrations')
               else:
                    userInfo=User.objects.create_user(username=uname,password=pwd,first_name=fname,last_name=sname,email=mail)
                    userInfo.save()
                    return redirect('login')
                    print("user created")
          else:

               print("password not matching")
               messages.info(request,"Password not matching")
               return redirect('registrations')
          return redirect('/')
     return render(request,"registration.html")

