from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('logout/', logoutFrom, name="logout"),
    path('signup/', signup, name="signup"),
    path('addblog/', add_Blog, name="addblog"),
    path('blogdetail/<slug>', blog_detail, name="blogdetail"),
    path('userblogs/', user_Blogs, name="userblogs"),
    path('blogdelete/<id>', blog_delete, name="blogdelete"),
    path('updateblog/<slug>', blog_update, name="updateblog"),
]