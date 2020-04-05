from django import forms

from blog.models import Category, BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'content', 'posted', 'language', 'categories']
