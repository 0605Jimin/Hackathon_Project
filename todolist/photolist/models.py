from tkinter import CASCADE
from distutils.text_file import TextFile
from django.db import models
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    photo = models.ImageField(blank=True, upload_to='photolist/post/%Y/%m/%d')
    place = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('photolist:photo_detail', args=[self.pk])

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.message