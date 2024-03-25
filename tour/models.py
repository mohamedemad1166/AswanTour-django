from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.
class Tours(models.Model):
    tour_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/tours')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tours'
        verbose_name_plural = 'Tours'

    def get_url(self):
        return reverse('tour_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.tour_name
