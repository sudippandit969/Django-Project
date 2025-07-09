from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect , HttpResponseForbidden
# Create your views here.

@never_cache
@login_required(login_url = "/login/")
def receipes(request):
    if request.method=="POST":
        data= request.POST
        receipe_name= data.get('receipe_name')
        receipe_description= data.get('receipe_description')
        receipe_image= request.FILES.get('receipe_image')
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        
        Receipe.objects.create(
            user=request.user,
            receipe_image= receipe_image,
            receipe_name= receipe_name,
            receipe_description= receipe_description
        )
        return  redirect('/receipes/')
    queryset = Receipe.objects.filter(user=request.user)
    
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes': queryset}
    return render(request, 'D:/All Projects/DJANGO-YOUTUBE/jangoproject/vege/templates/receipes.html', context)

@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if queryset.user == request.user:
        queryset.delete()
    return redirect('/receipes/')

@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    if queryset.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this recipe.")
    if request.method=="POST":
        data= request.POST
        receipe_name= data.get('receipe_name')
        receipe_description= data.get('receipe_description')
        receipe_image= request.FILES.get('receipe_image')
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect('/receipes/')
    context = {'receipe':queryset}
    return render(request, 'D:/All Projects/DJANGO-YOUTUBE/jangoproject/vege/templates/update_receipes.html', context)

def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username__iexact=username).exists():
            messages.info(request, "Invalid username!")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.info(request, "Invalid password!")
            return redirect('/login/')
        else:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('/receipes/')
    
    return render(request, 'D:/All Projects/DJANGO-YOUTUBE/jangoproject/vege/templates/login.html')

@never_cache
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        request.session.flush()  # Clear all session data
    response = HttpResponseRedirect('/login/')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "username already exists!")
            return redirect('/register/')
            
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully!")
        return redirect('/login/')

    return render(request , 'register.html')

def social(request):
    return render(request, 'D:/All Projects/DJANGO-YOUTUBE/jangoproject/home/templates/html/socialmedia.html')
