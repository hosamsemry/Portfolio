from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Project

def home(request):
    return render (request, 'index.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = [
        {
            "name": "Social Website",
            "github": "https://github.com/hosamsemry/Social-Website",
            "description": "This Django project is a social app that allows users to register, log in, and interact with each other through various features such as following other users, liking images, and bookmarking images.",
        },
        {
            "name": "E-Commerce API",
            "github": "https://github.com/hosamsemry/E-commerce",
            "description": "An e-commerce API built with Django Rest Framework. This project includes functionalities for managing users, products, carts, orders, order items, collections, product images, product reviews, and addresses.",
        },
        {
            "name": "Parking Reservation System",
            "github": "https://github.com/hosamsemry/smart-garage",
            "description": "The Parking Reservation System project is a web application developed using Django and Django Rest Framework (DRF) for creating RESTful APIs. The project aims to provide easy managing and reserving parking spaces in garages efficiently.",
        },
        {
            "name": "Task Manager",
            "github": "https://github.com/hosamsemry/Task-Manager",
            "description": "Task Manager API is a Django project that provides APIs for managing projects, tasks, comments, and activity logs.",
        }
    ]
    return render(request, 'projects.html', {'projects': projects})
    

def cv(request):
    return render(request, "cv.html")