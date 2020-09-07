from django import forms
from django.urls import reverse
from Blog.models import Blog, BlogComment, BlogUsers
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model=Blog
        fields = [
            'name',
            'description',

        ]

        widgets = {
            'message': forms.Textarea(attrs={'rows': 2 ,'col':4})

        }



    def __init__(self, *args, **kwargs):
        super(CreateBlogForm, self).__init__(*args, **kwargs)
        # self.fields['author'].initial = self.request.user
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',"rows":2})


    def clean_author(self):
        if not self.cleaned_data['author']:
            return User()
        return self.cleaned_data['author']


# class CommentForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super(CommentForm, self).__init__(*args, **kwargs)
#         self.fields['description'].widget.attrs.update({'class': 'form-control', "rows":2})
#
#     class Meta:
#         model=BlogComment
#         fields=["description",]



# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    bio = forms.CharField(max_length=500, help_text="Please Enter the bio details here.")

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'bio'
            ]

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control', "rows": 2})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]