from django.shortcuts import render
from requests import request

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def add_Blog(request):
    return render(request, 'addBlog.html')