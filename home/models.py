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
 

class Leader(models.Model):
    leaderImg=models.ImageField(upload_to = "pics", blank = True)
    leaderName=models.CharField(max_length=100)
    leaderPosition=models.CharField(max_length=100)
    leaderDesc=models.CharField(max_length=1000)

class contactPage(models.Model):
    contactHeader = models.CharField(max_length=100)
    contactParagraph = models.CharField(max_length=100)

class contactDetails(models.Model):
    contactName = models.CharField(max_length=100)
    contactImg = models.ImageField(upload_to = "contact", blank = True)
    contactPosition = models.CharField(max_length=100)
    contactPhone = models.CharField(max_length=100)
    contactEmail = models.CharField(max_length=100)

class Academic(models.Model):
    acadsImg=models.ImageField(upload_to = "acads", blank = True)
    acadsHead=models.CharField(max_length=100)
    acadsDesc=models.CharField(max_length=1000)

class Extras(models.Model):
    extraHeader = models.CharField(max_length=100)
    extraImg = models.ImageField(upload_to = "extras", blank = True)
    extraParagraph = models.CharField(max_length=1000)
    extraHref = models.CharField(max_length=1000)
    extraHrefTitle = models.CharField(max_length=100)