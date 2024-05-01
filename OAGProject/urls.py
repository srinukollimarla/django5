"""
URL configuration for OAGProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpResponseNotFound
from django.urls import path, include
from. import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("adminapp.urls")),
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("contactus", views.contactus, name='contactus'),
    path("register", views.register, name="register"),
    path("artistlogin", views.artistlogin, name="artistlogin"),
    path("artistregister", views.artistregister, name="artistregister"),
    path("adminhome", views.adminhome,name="adminhome"),
    path("about", views.about,name="about"),
    path('favicon.ico', lambda request: HttpResponseNotFound(), name='favicon'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path("artist_home",views.artist_home,name="artist_home"),
    path('artist', views.artist, name='artist'),

]


