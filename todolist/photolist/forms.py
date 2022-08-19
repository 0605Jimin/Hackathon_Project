from xml.etree.ElementTree import Comment
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['photo', 'title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
