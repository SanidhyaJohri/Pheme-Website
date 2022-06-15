from distutils.command.upload import upload
from django.db import models

# Create your models here.
class WelcomeMessage(models.Model):
    welcomeHeader=models.CharField(max_length=1000)
    welcomeParagraph=models.CharField(max_length=10000)

class AboutContent(models.Model):
    aboutName=models.CharField(max_length=100)
    aboutUs=models.CharField(max_length=100)
    aboutDescription=models.CharField(max_length=10000)

class BlogCard(models.Model):
    blogImg = models.ImageField(upload_to = "pics", blank = True)
    blogDate = models.DateTimeField(auto_now_add = True)
    blogHref = models.CharField(max_length=100)
    blogHeading = models.CharField(max_length=100)

