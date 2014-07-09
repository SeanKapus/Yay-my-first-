from django import forms
from django.forms import ModelForm
from book.models import Author, Comment, Tag


class BlogPostForm(forms.Form):
    author = forms.ModelChoiceField(Author)
    comment_body = forms.CharField()

class AuthorForm(ModelForm):
    class Meta:
        model = Author


class CommentForm(ModelForm):
    class Meta:
        model = Comment


class TagForm(ModelForm):
    class Meta:
        model = Tag
