from django.shortcuts import render
from App.data.readData import ReadData

# Create your views here.
def index(request):
    return render(request,'Pages/home.html')

def project(request):
    context = {
        'data' : ReadData.Read(),
    }
    return render(request,'Pages/project.html',context)