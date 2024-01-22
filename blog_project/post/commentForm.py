
from .models import Comment
from django import forms

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['name','post'] # eta new add kora hoicha.
        # fields = ['name','email','body']
        