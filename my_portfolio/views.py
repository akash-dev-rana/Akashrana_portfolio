from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")

        full_message = f"""
                        Name: {name}
                        Email: {email}

                        Message:
                            {message}
                        """

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
            messages.error(request, f"Message could not be sent: {e}")

        return redirect("/")

    return render(request, "index.html")
