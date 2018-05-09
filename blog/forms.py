from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=100)
    image = forms.URLField()
    content = forms.Textarea()
    posted = forms.DateField()
    language = forms.CharField(max_length=15)
    category = forms.CharField(max_length=15)
