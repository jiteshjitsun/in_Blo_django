import imp
import re
from django.shortcuts import redirect, render
from matplotlib.style import context
# from matplotlib.style import context
# from requests import request
from .forms import *
from django.contrib.auth import logout

def logoutFrom(request):
    logout(request)
    return redirect('/')

# Create your views here.
def home(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def blog_detail(request, slug):
    context = {}
    # try:
    blog_obj = Blog.objects.filter(slug = slug).first() 
    context['blog_obj'] = blog_obj
    print(blog_obj.content)
    # except Exception as e:
    #     print(e)
    print("ejmikj")
    return render(request, 'blog_detail.html', context)

def user_Blogs(request):
    context = {}
    # try:
    blog_ob = Blog.objects.filter(user = request.user)
    context['blog_ob'] = blog_ob
    # print(blog_obj.content)
    # except Exception as e:
    #     print(e)
    # print("ejmikj")
    return render(request, 'user_blog.html', context)

def blog_delete(request, id):
    blog_o = Blog.objects.get(id=id)
    if blog_o.user == request.user:
        blog_o.delete()
    return redirect('/userblogs/')


def blog_update(request, slug):
    context = {}


    blog_o = Blog.objects.get(slug=slug)
    initial_dict = {'content': blog_o.content}
    form = BlogForm(initial=initial_dict)
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
    if blog_o.user != request.user:
        return redirect('/')
    
    context['blog_o'] = blog_o
    context['form'] = form
    return render(request, 'update_blog.html', context)

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