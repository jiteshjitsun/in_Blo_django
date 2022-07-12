import imp
import re
from django.shortcuts import redirect, render
# from matplotlib.style import context
# from requests import request
from .forms import *

# Create your views here.
def home(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def blog_detail(request, slug):
    return render(request, 'blog_detail.html')

def signup(request):
    return render(request, 'signup.html')

def add_Blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            Blog.objects.create(
                user = user, title = title,
                content = content, image = image
            )

            return redirect('/addblog/')
    except Exception as e:
        print(e)
    return render(request, 'addBlog.html', context)