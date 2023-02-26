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
    project = Project.objects.all().order_by('-add_date')
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
        recipient = request.POST.get('email')

        mail1 = (subject,message,EMAIL_HOST_USER,[EMAIL_HOST_USER])
        mail2 = ('Message submitted',confirm_message,EMAIL_HOST_USER,[recipient])

        send_mass_mail((mail1,mail2),fail_silently=False)
    context = {'education':education,'skill':skill,'project':project,'language':language,'work':work}
    return render(request, "index.html",context)
    
