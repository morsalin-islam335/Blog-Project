from django.shortcuts import render, redirect

# Create your views here.

from .categoryForm import CategoryForm

def addCategory(request):
    if(request.method == "POST"):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'category.html', {"form":CategoryForm()})
