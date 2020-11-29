"""
Blog Forms
"""
from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    """Form to Share by email a Post
    """

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Form to readers commenting a Post
    """

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
