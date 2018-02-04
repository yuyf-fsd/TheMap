from django.shortcuts import render
from django.http import HttpResponse #add

# Create your views here.

def index(request): #add sample API
    return HttpResponse("Hello API !") #add
