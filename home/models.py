from django.db import models

# Create your models here.
class WelcomeMessage(models.Model):
    welcomeHeader=models.CharField(max_length=1000)
    welcomeParagraph=models.CharField(max_length=10000)