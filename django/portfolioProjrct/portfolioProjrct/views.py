from django.shortcuts import render
from django.http import  HttpResponse

# def about(request):
#     return render(request, 'about')

def zen(request):
    # return HttpResponse("Corgis are awesome! <a href='/hello'>Go to homepage</a>")
    return render(request, 'zen_mockup.html')

# def javapic(request):
#     return render(request, 'javapic.html')

# def javapic_jquery(request):
#     return render(request, 'javapic_files/')