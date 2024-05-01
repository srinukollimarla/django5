from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect



def home(request):
    return render(request, "home.html")


def add_artist(request):
    return render(request, "add_artist.html")


def sculptures(request):
    return render(request, "sculptures.html")


def artists(request):
    return render(request, "artists.html")


def about(request):
    return render(request, "about.html")


def contactus(request):
    return render(request, "contactus.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def artistlogin(request):
    return render(request, "artistlogin.html")


def adminhome(request):
    return render(request, "adminhome.html")


def artistregister(request):
    return render(request, "artistregister.html")


def artist_home(request):
    return render(request, "artist_home.html")


def artist(request):
    return render(request, "artist.html")
