from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Message from SimpleBlog.com'
            emailFrom = form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
            message = '%s\n%s\n%s' %(comment, name, emailFrom)
            send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
            return HttpResponse('<center><b><h1>Thanks for contacting us!</h1></b></center>')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})