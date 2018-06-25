from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return {
            'name': self.name,
            'slug': self.slug
        }


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.URLField()
    content = models.TextField()
    posted = models.DateField()
    language = models.CharField(max_length=15)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return {
            'title': self.title,
            'slug': self.slug,
            'image': self.image,
            'content': self.content,
            'posted': self.posted,
            'language': self.language,
            'categories': self.categories
        }
