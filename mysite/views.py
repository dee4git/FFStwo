from . import views
from django.contrib import admin
from django.shortcuts import render, redirect


def home(request):
    """The homepage function"""
    return render(request, 'home.html', )


def working(request):
    """This function redirects to not yet implemented functions."""
    return render(request,'working.html')