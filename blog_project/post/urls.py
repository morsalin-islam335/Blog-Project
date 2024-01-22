from django.urls import path

from post import views
urlpatterns = [
    # path("addCategories/", addCategories, name= 'addCategories'),
    path("add_post/", views.AddPost.as_view(), name='add_post'),
    path("edit_post/<int:id2>",views.EditPost.as_view(), name='edit_post'),
    path("delete_post/<int:id>", views.DeletePost.as_view(), name='delete_post'),
    path("details_post/<int:id>", views.Details.as_view(), name='post_details'),
]
