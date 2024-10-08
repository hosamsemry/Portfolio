from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Project

def home(request):
    return render (request, 'home.html')


def about(request):
    return render(request, 'about.html')

def projects(request): 
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
    

""" def contact(request):
    return render(request, "contact.html") """

def cv(request):
    return render(request, "cv.html")