"""
URL configuration for jangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import * 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    
    path('',home, name="home"),
    path('receipes/', receipes, name="receipes"),
    path('delete_receipe/<id>/' , delete_receipe , name="delete_receipe"),
    path('update_receipe/<id>/' , update_receipe , name="update_receipe"),
    # path('success_page/',success_page, name="success_page"),
    path('about/',about, name="about"),
    path('social/', social, name="social"),
    path('contact/',contact, name="contact"),
    path('admin/', admin.site.urls),
    path('login/',login_page, name="login_page"),
    path('register/',register_page, name="register_page"),
    path('logout/',logout_page, name="logout_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()    