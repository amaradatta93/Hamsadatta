from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, db_index=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.URLField()
    content = models.TextField()
    posted = models.DateField()
    language = models.CharField(max_length=15)
    categories = models.ManyToManyField(Category)


