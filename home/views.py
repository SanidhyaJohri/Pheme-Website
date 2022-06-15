from django.shortcuts import render, HttpResponse, redirect
from django.http import response, HttpResponse
from .models import *
# Create your views here.
def index(request):

    welcome=WelcomeMessage.objects.all()[0]
    welcomeHeader=welcome.welcomeHeader
    welcomeParagraph=welcome.welcomeParagraph

    context={
        "welcomeHeader": welcomeHeader,
        "welcomeParagraph": welcomeParagraph,
    }
    
    return render (request, "index.html",context)

def about(request):
    return render (request, "about.html")