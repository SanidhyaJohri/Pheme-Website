from django.shortcuts import render, HttpResponse, redirect
from django.http import response, HttpResponse
from .models import *
# Create your views here.
def index(request):

    welcome=WelcomeMessage.objects.all()[0]
    welcomeHeader=welcome.welcomeHeader
    welcomeParagraph=welcome.welcomeParagraph

    blogCard = BlogCard.objects.all()
    

    context={
        "welcomeHeader": welcomeHeader,
        "welcomeParagraph": welcomeParagraph,
        "blogCard" : blogCard
    }

    return render (request, "index.html",context)

def about(request):
    about=AboutContent.objects.all()[0]
    aboutName=about.aboutName
    aboutUs=about.aboutUs
    aboutDescription=about.aboutDescription

    context={
        "aboutName": aboutName,
        "aboutUs": aboutUs,
        "aboutDescription":aboutDescription
    }
    return render (request, "about.html",context)

