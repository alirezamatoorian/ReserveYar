from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Resources(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='resources')
    location=models.TextField()
    description=models.TextField()
    capacity=models.PositiveIntegerField(default=0)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

