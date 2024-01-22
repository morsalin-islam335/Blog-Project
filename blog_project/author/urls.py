from django.urls import path

from author import views
urlpatterns = [
    path('sign_up/', views.Signup, name='sign_up'),
    path('login/', views.Login.as_view(), name = 'login'),
    path('logout/', views.userLogout, name = 'logout'),
    # path('logout/', views.Logout.as_view(), name = 'logout'),
    path('editProfile/', views.updateProfile, name = 'editProfile'),
    path("profile/", views.Profile, name = 'profile'),
    path("changePassword/", views.changePassword, name = "changePassword")
]
