from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse('dashboard:details', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('id',)


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.URLField()
    content = models.TextField()
    posted = models.DateField()
    language = models.CharField(max_length=15)
    categories = models.ManyToManyField(Category, blank=False)

    def as_dict(self):
        return {
            'id': self.pk,
            'title': self.title,
            'slug': self.slug,
            'image': self.image,
            'content': self.content,
            'posted': self.posted,
            'language': self.language
        }

    class Meta:
        ordering = ('posted',)
