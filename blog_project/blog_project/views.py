from django.shortcuts import render
from post.models import Post

from categories.models import Category

def homepage(request, category_slug = None):
    data = Post.objects.all()
    status = False
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug) # first time we we catch slug with category_slug
        data = Post.objects.filter(category = category) # then select that category with filter function
        status  = True
    categories = Category.objects.all()
    return render(request, "homepage.html", {"postData":data, 'categories': categories, "status": status, 'total': len(data)})
    '''
    first a data = sob post nibo jodi kono kichu return select na kora tahola
    then check korbo category_slug None ki na.
        jodi none na hoy tahola cateogry_slug onujay filter kora Category select korbo
        then sei category onujay filter kora  Post nia filter kora data ta assign korbo ( eta ager data chenge hoia jaba)
        finally sob gulo category ja many to many relation hisaba post a thakta para ta
                categories a assign korbo
                    categories = Category.objects.all() # sob category
        then last a data ar categories context kora render korbo

    '''



