from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#how to print a text
# def demo(request):
#     return HttpResponse("Happy Newyear")

#how to show an htmlpage
# def demo(request):
#     return HttpResponse("Happy Newyear")
# def demo(request):
#     return render(request,"home.html")
from . models import NewsandArticles,explore
def demo(request):
    # name="india"
    # return render(request,"about.html",{"obj":name})
    obj = NewsandArticles.objects.all()
    obj2=explore.objects.all()
    return render(request, "index.html",{"result":obj,"result2":obj2})

# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     return render(request,"result.html",{"resul":res})

