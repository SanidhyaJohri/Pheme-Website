from django.db import models

# Create your models here.
class WelcomeMessage(models.Model):
    welcomeHeader=models.CharField(max_length=1000)
    welcomeParagraph=models.CharField(max_length=10000)

class AboutContent(models.Model):
    aboutName=models.CharField(max_length=100)
    aboutUs=models.CharField(max_length=100)
    aboutDescription=models.CharField(max_length=10000)

