from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

def index(request):
    context={
        'variable1':'my name is princyyyyyy',
        'variable2':'learn django for full stack'
    }
    messages.success(request,"this is a success message")
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')

    #return HttpResponse("this is about page")


def services(request):
    return render(request,'services.html')
   # return HttpResponse("this is services page")


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your profile was updated.") 
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")