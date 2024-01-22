from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='post/media/uploads/',blank= True, null = True)


    def __str__(self):
        return self.title
    


class Comment(models.Model):
    # One to many relationship
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name  = 'comments') # we can access title, content etc through related name
    name = models.CharField(max_length = 50)
    # email = models.EmailField() #eta bad dewa hoicha
    body = models.TextField(verbose_name = 'comment')
    comments_time = models.DateTimeField(auto_now_add = True) # jokhon kau ekjon comment korba sei time captue hoiba

    def __str__(self):
        return f'comments by {self.name}'

        