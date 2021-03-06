import self
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


class BlogUsers(models.Model):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='ref_b')
    bio = models.TextField(max_length=500, help_text="Please Enter the bio details here.")

    class Meta:
        ordering = ["user", "bio"]

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user.username





class Blog(models.Model):

    name = models.CharField(max_length=500)
    author = models.ForeignKey(BlogUsers, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=5000, help_text="Please Enter the blog description here.")
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class BlogComment(models.Model):

    description = models.TextField(max_length=75, help_text="Please Enter the comment about blog here.")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):

        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.blog.id)])

class A(models.Model):
   def get_B(self):
       try:
          return self.b
       except:
           return BlogUsers.objects.create(
               user=self,)


