from django.shortcuts import render
from django.http import  HttpResponse

def forum(request):
    return render(request, 'Forum.html')

def zen(request):
    return render(request, 'zen_mockup.html')

def javapic(request):
    return render(request, 'jsindex.html')

def jquerypic(request):
    return render(request, 'jqindex.html')

def home(request):
    return render(request, 'homepg.html')