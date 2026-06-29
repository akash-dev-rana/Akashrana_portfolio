from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import contact
from django.core.mail import EmailMessage
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
        try:
            email_message = EmailMessage(
                subject=f"Portfolio Contact Form - {name}",
                body=full_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],
            )

            email_message.send(fail_silently=False)

            messages.success(request, "Message sent successfully!")

        except Exception as e:
            print("EMAIL ERROR:", e)
            messages.error(request, "Message could not be sent. Please try again later.")

        return redirect("/")

        return render(request, "index.html")


