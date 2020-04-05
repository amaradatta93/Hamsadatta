from django import forms
from django.views.generic.edit import CreateView

from .forms import BlogPostForm
from .models import BlogPost


class BlogPostCreate(CreateView):
    model = BlogPost
    form_class = BlogPostForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(BlogPostCreate, self).get_form(form_class)
        form.fields['posted'].widget = forms.TextInput(attrs={'placeholder': 'mm/dd/yyyy'})
        return form

    def form_valid(self, form):
        slug = str(form.instance.title).replace(" ", '-').lower()
        form.instance.slug = slug
        return super(BlogPostCreate, self).form_valid(form)
