from django.urls import path

from categories import views
urlpatterns = [
    # path("addCategories/", addCategories, name= 'addCategories'),
    path("add_category/", views.addCategory, name='add_category'),
    
]
