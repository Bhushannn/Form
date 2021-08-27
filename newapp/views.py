from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("THANKS FOR CONTACTING US")

    return render(request,'index.html')
