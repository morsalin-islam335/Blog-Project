from typing import Any
from django.shortcuts import render, redirect

# Create your views here.
from author import authorForm
from django.http import HttpResponse

# def addAuthor(request):
#     if(request.method == "POST"):
#         form = ProfileForm(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return redirect("add_author")
#     form = ProfileForm()
#     return render(request, "author.html",{"form": form})            





def Signup(request):
    if request.method == 'POST':
        author_form = authorForm.RegistrationForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            messages.success(request, "Congratulations!  Account Create Successfully")

            return redirect('homepage')
        
    author_form = authorForm.RegistrationForm()
    return render(request, 'registration.html', {'form' : author_form})



#import login form
from django.contrib.auth.forms import AuthenticationForm
# import authenticate that will be check if a user is valid or not

from django.contrib.auth import authenticate, login

#import message

from django.contrib import messages

# def loginForm(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request = request, data = request.POST)

#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_password = form.cleaned_data['password']

#             user = authenticate(username = user_name, password = user_password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Login Successfully!")
                
#                 return redirect("profile")
#             else:
                
#                 messages.warning(request, "log in information is incorrect")

#     else:
#         form  = AuthenticationForm()
#     return render(request, 'login.html', {"form":form})


from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class Login(LoginView):
    model = AuthenticationForm # this is not mandatory.  LoginView has a built-in AuthenticationForm
    template_name = 'login.html'

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def from_valid(self, form):
        messages.success(self.request, "login information incorrect.")
        return super().from_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, "Login Successfully!")
        return reverse_lazy("profile")
    
    # success_url = reverse_lazy("profile")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'Log In Page'
        return context
    








from django.contrib.auth import logout

def userLogout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        messages.warning(request, 'logout successfully')
        return redirect("login")



# from django.contrib.auth.views import LogoutView
# from django.contrib.auth.models import User
# class Logout(LogoutView):

#     model = User
#     # def form_valid(self, form):
#     #     # messages.success(self.request, "logout successfully")

#     #     return super().form_valid(form)
    
#     success_url_allowed = reverse_lazy("login")


#import login required
    
# from django.contrib.auth.decorators import login_required

#import 

from . updateProfile import UpdateProfile


def updateProfile(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = UpdateProfile(request.POST, instance = request.user)

            if form.is_valid():
                messages.success(request, "Profile Update  Successfully")
                form.save()
                return redirect("profile")
        else:
            form = UpdateProfile(instance = request.user)
        return render(request,"updateProfile.html",{"form":form})
    else:
        return redirect("login")
    




from post.models import Post

def Profile(request):
    if request.user.is_authenticated:
        data = Post.objects.filter(author = request.user)
        return render(request, 'profile.html', {"data": data})
    else:
        return redirect("login")
    

#import password set form
    
from django.contrib.auth.forms import SetPasswordForm

# import  update session auth hash


from django.contrib.auth import update_session_auth_hash


def changePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user = request.user, data =  request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, "Password Updated Successfully")

                return redirect("profile")
        else:
            form = SetPasswordForm(request.user)
        return render(request, 'passwordChange.html',{"form": form})
    else:
        return redirect("login")





