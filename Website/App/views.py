from django.shortcuts import render
from App.data.readData import *

# Create your views here.
def index(request):
    return render(request,'Pages/home.html')

def project(request):
    context = {
        'data' : getData(),
    }
    return render(request,'Pages/project.html',context)

def aboutwe(request):
    return render(request,'Pages/aboutwe.html')