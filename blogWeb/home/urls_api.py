from django.urls import path

from home.views_api import LoginView, RegisterView
from .views import *

urlpatterns = [
    path('login/', LoginView),
    path('register/', RegisterView)
]