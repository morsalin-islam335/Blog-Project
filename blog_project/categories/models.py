from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 70)

    slug = models.SlugField(max_length = 1000, null = True, blank = True, unique = True)


    def  __str__(self):
        return self.name
