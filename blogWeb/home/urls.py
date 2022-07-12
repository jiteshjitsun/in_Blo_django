from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('addblog/', add_Blog, name="addblog"),
    path('blog-detail/<slug>', blog_detail, name="blog_detail"),
]