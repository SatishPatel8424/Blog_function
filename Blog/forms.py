from django import forms
from django.urls import reverse
from Blog.models import Blog, BlogComment


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model=Blog
        fields= "__all__"

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control', "rows":2})

    class Meta:
        model=BlogComment
        fields=["description",]

