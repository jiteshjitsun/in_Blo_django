from django.db import models
from django.contrib.auth.models import User
from django.forms import SlugField
from numpy import true_divide
from .misc import *

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, blank=True, null= True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to = 'blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_Slug(self.title)
        super(Blog,self).save(*args, **kwargs)

