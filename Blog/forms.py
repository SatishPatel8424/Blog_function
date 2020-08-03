from django import forms
from django.urls import reverse
from Blog.models import Blog, BlogComment


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model=Blog
        fields= "__all__"
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4 }),
        }

    def __init__(self, *args, **kwargs):
        super(CreateBlogForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control', "rows":2})

    class Meta:
        model=BlogComment
        fields=["description",]

