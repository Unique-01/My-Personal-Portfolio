from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    image = models.ImageField( upload_to='img/', height_field=None, width_field=None, max_length=None)
    tech_used = models.CharField(max_length=250, null=True,blank=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    date = models.CharField(max_length=150)
    role = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.website

class EducationExperience(models.Model):
    date = models.CharField(max_length=150)
    course = models.CharField(max_length=150)
    school = models.CharField(max_length=250)

    def __str__(self):
        return self.course

class LanguageExperience(models.Model):
    language = models.CharField(max_length=150)
    level = models.CharField(max_length=150)

    def __str__(self):
        return self.language

class Skill(models.Model):
    skill_name = models.CharField(max_length=150)
    level = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.skill_name
