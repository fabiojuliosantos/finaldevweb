from django.shortcuts import render
from django.views.generic import TemplateView

def inicial(request) :
    return render(request, 'base.html')