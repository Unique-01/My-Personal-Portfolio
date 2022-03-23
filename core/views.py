from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
# from . import forms
from django.http import HttpResponse
from myportfolio.settings import EMAIL_HOST_USER
from .models import *
from django.views import generic

# Create your views here.

def allparameters(request):
    education = EducationExperience.objects.all()
    skill = Skill.objects.all()
    project = Project.objects.all()
    language = LanguageExperience.objects.all()
    work = WorkExperience.objects.all()

#    The contact mail processing
    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = {
                'email':request.POST.get('email'),
                'message':request.POST.get('message')
            }
        message = '\n'.join(body.values())

        confirm_message = 'The admin have received your message and will get back to you as soon as possible'
        recepient = request.POST.get('email')

        mail1 = (subject,message,EMAIL_HOST_USER,[EMAIL_HOST_USER])
        mail2 = ('Message submitted',confirm_message,EMAIL_HOST_USER,[recepient])

        send_mass_mail((mail1,mail2),fail_silently=False)

        # send_mail(subject,message,EMAIL_HOST_USER,[EMAIL_HOST_USER],fail_silently=False)
        # send_mail('Message submitted',confirm_message,EMAIL_HOST_USER,[recepient],fail_silently=False)

    context = {'education':education,'skill':skill,'project':project,'language':language,'work':work}
    return render(request, "index.html",context)
    
   
    # contact_form = forms.ContactForm()
    # if request.method == 'POST':
    #     contact_form = forms.ContactForm(request.POST)
    #     if contact_form.is_valid():
            # subject = contact_form.cleaned_data['subject']
            # body = {
            #     'email':contact_form.cleaned_data['email'],
            #     'message':contact_form.cleaned_data['message']
            # }
            # message = '\n'.join(body.values())
            # send_mail(subject,message,'admin@example.com',['admin@example.com'],fail_silently=False)
    # contact_form = forms.ContactForm()
    # return render(request, "index.html", {'contact_form':contact_form})
    
            