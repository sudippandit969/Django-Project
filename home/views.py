# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return render(request , "receipes.html")

# def contact(request):
#     return render(request , "html/contact.html")

# def about(request):
#     return render(request , "D:/All Projects/DJANGO-YOUTUBE/jangoproject/home/templates/html/about.html")

# # def success_page(request):
# #      return HttpResponse("Hey this is a success page")
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "receipes.html")  # From vege/templates/

def contact(request):
    return render(request, "html/contact.html")  # From home/templates/html/

def about(request):
    return render(request, "html/about.html")  # ✅ FIXED: No full path here

# Optional: this works fine if uncommented
# def success_page(request):
#     return HttpResponse("Hey this is a success page")
