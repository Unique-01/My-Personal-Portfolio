from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Project)
admin.site.register(WorkExperience)
admin.site.register(EducationExperience)
admin.site.register(LanguageExperience)
admin.site.register(Skill)
