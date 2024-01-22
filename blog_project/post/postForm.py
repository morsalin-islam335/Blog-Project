from django import forms

from . models import Post

from categories.models import Category

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        exclude  = ['author']

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )



