from django import forms
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import BlogPostForm
from .models import BlogPost


class BlogPostClean:
    model = BlogPost
    form_class = BlogPostForm

    def get_object(self, *args, **kwargs):
        blog = get_object_or_404(BlogPost, pk=self.kwargs['blog_id'])
        return blog

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super().get_form(form_class)
        form.fields['posted'].widget = forms.TextInput(attrs={'placeholder': 'mm/dd/yyyy'})
        return form

    def form_valid(self, form):
        slug = str(form.instance.title).replace(" ", '-').lower()
        form.instance.slug = slug
        return super().form_valid(form)


class BlogPostCreate(BlogPostClean, CreateView):
    def get_object(self, *args, **kwargs):
        pass


class BlogPostUpdate(BlogPostClean, UpdateView):
    pass


class BlogPostDelete(BlogPostClean, DeleteView):
    form_class = None
    success_url = reverse_lazy('dashboard:posts')

    def get_form(self, form_class=None):
        pass

    def form_valid(self, form):
        pass
