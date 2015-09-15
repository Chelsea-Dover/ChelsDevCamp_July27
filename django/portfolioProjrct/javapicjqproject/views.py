from django.shortcuts import render

def jqjavapic(request):
    return render(request, 'jqindex.html')

def jqoin(request):
    return render(request, 'jqjoin.html')

def jqgallery(request):
    return render(request, 'gallery.html')