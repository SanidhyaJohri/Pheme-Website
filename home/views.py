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

    leader=Leader.objects.all()
    context={
        "aboutName": aboutName,
        "aboutUs": aboutUs,
        "aboutDescription":aboutDescription,
        "leader":leader
    }
    return render (request, "about.html",context)


def contact(request):
    contactMessage = contactPage.objects.all()[0]
    contactHeader = contactMessage.contactHeader
    contactParagraph = contactMessage.contactParagraph
    contactdetails=contactDetails.objects.all()
    context={
        "contactHeader" : contactHeader,
        "contactParagraph" : contactParagraph,
        "contactdetails":contactdetails
    }
    return render (request, "contact.html",context)

def Acads(request):
    acads=Academic.objects.all()[0]
    acadsHead=acads.acadsHead
    acadsDesc=acads.acadsDesc
    acadsImg=acads.acadsImg


    context={
        "acadsHead":acadsHead,
        "acadsDesc":acadsDesc,
        "acadsImg":acadsImg

    }
    return render(request, "Acads.html", context)

def Extra(request):
    extras = Extras.objects.all()

    context={
        "extras": extras
    }
    return render(request, "Extra.html", context)

def project(request):
    return render(request, "project_details.html")

def events(request):
    event=Event.objects.all()

    context={
        "events": event,
    }
    return render(request, "events.html", context)