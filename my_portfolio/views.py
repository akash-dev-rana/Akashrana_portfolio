from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def contacts(request):
    if(request.method == "POST"):
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')
        date =  datetime.today()
        print(name)
        full_message = f"""
                Name: {name}
                Email: {email}
                Message: {message}
                """
        send_mail(
            subject="New Portfolio Contact Form Message",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["terrorking487@gmail.com"],
        )
        messages.success(request, " Your message has been sent successfully!")
    return render(request,"index.html")


