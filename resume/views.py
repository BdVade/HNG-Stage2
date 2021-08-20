import smtplib

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


def resume_page(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        context = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "message": message
        }
        email_message = render_to_string('mail.txt', context)
        try:
            send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, ["victoraderibigbe03@gmail.com"],
                      fail_silently=False)
        except smtplib.SMTPException:
            messages.warning(request, 'Something went wrong. Please try again')
            return redirect(request.META.get('HTTP_REFERER'))

        messages.success(request, 'Your message has been received. I will be in contact with you very soon!')
        return redirect(request.META.get('HTTP_REFERER'))
