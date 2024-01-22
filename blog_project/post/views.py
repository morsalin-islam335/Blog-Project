from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

# Create your views here.
from . models import Post


from . postForm import PostForm
# def addPost(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         form.instance.author = request.user
#         if form.is_valid():
#             form.save()
#             print("add post successfully")
#             return redirect('homepage')
#     form = PostForm()
#     return render(request, 'post.html',{"form":form})

from django.views.generic import CreateView  # eta view create korta import korta hoba
from django.urls import reverse_lazy # we need this to work like redirect

from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name = 'dispatch')
class  AddPost(CreateView):
    model = Post
    template_name = 'post.html'
    form_class = PostForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)








       
from . import models


# def editPost(request, id): 
#     edited_post = Post.objects.get(pk = id) # we receive here previous edited post 
    

#     if(request.method == "POST"):#post request

#         form = PostForm(request.POST,instance= edited_post)

#         if form.is_valid():
#             form.save()
#             return redirect("homepage")
#     else:
#         form = PostForm(instance = edited_post)
#         return render(request, 'post.html', {"form": form})        
    

from django.views.generic import UpdateView

@method_decorator(login_required, name = 'dispatch')
class EditPost(UpdateView):
    model = Post
    template_name ='post.html'
    form_class = PostForm
    pk_url_kwarg = 'id2'
    success_url = reverse_lazy('homepage')



# def deletePost(request, id):
#     data =Post.objects.get(pk = id)
#     data.delete() # delete from database
#     return redirect("homepage")
    

from django.views.generic import DeleteView

@method_decorator(login_required, name = 'dispatch')
class DeletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg ='id'



from .commentForm import CommentsForm
from django.views.generic import DetailView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name = 'dispatch')
class Details(DetailView):
    model = Post
    template_name = 'post_details.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
            post = self.get_object() # or self.get_object
            Form = CommentsForm(data = self.request.POST) # comment form er data soho comment form
            if Form.is_valid():
                newComment = Form.save(commit = False)
                newComment.post = post # jakhana comment korba sei post
                newComment.name = self.request.user # eta notun add kora hoicha
                newComment.save()

            return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.object #  specific primary key dia sei model er ekta object asba
        
        # ekhon functon base view er moto kora kaj korbo
        # if self.request.method == "POST": # user jodi comment kora tahola er vitor er kaj gulo hoiba
            # Form = CommentsForm(data = self.request.POST) # comment form er data soho comment form
            # if Form.is_valid():
            #     newComment = Form.save(commit = False)
            #     newComment.post = post # jakhana comment korba sei post
            #     newComment.save()
        # else:
        #     Form = CommentsForm()

        Form = CommentsForm
        comments = post.comments.all # comments is related name of Comment model

        context['commentForm'] = Form
        context['comments'] = comments

        return context
    def get_success_url(self):
        return reverse_lazy("post_details")
    

