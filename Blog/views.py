from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.serializers import json
from django.http import HttpResponseRedirect, JsonResponse, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
import json
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView

from Blog.forms import CreateBlogForm,CommentForm,ProfileForm,SignUpForm
from .models import Blog,BlogUsers
from django.views import View


# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )


class BlogList(View):
    def get(self, request):
        if not request.user.is_authenticated:
            blogs = Blog.objects.all().order_by('-post_date')
            blog_list = serializers.serialize('json', blogs)
            return JsonResponse(blog_list, safe=False)


        else:
            user = request.user
            blogger = BlogUsers.objects.get(user=user)
            blogs = Blog.objects.filter(author=blogger).order_by('-post_date')
            blog_list1 = serializers.serialize('json', blogs)
            return JsonResponse(blog_list1, safe=False)



class BlogDetail(View):
    def get(self, request,pk):
        blog1 = Blog.objects.get(pk=pk)
        most_recent = Blog.objects.order_by('-timestamp')[:3]

        context = {
            'blog1': blog1,
        }
        return render(request, "blog/blog_detail.html", context)


class BloggerList(View):
    def get(self, request):
        BlogAuthor1 = BlogUsers.objects.all()
        return render(request, 'blog/blogauthor_list.html', {'BlogAuthor1': BlogAuthor1})



class BlogListbyAuthor(View):
    def get(self, request,pk):

        blogger = BlogUsers.objects.get(pk=pk) #Bloger
        blogs = Blog.objects.filter(author=blogger)
        context = {'blog_author': blogger,
                   'blogs': blogs}

        return render(request, "blog/blog_list_by_author.html", context)


class CreateBlogView(View):
    form_class = CreateBlogForm
    template_name = "blog/create_blog.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        return render(self.request, self.template_name, {"form": form})


    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False, "errors" : form.errors}, status=400)


class BlogDetail(View):
    def get(self, request,pk):
        blog = Blog.objects.get(id=pk)
        form = CommentForm()
        comments = blog.blogcomment_set.all()
        return render(request,
                      "blog/blog_detail.html",
                      context={"form":form,
                               "comments": comments,
                               "blog": blog})


    def post(self,request, pk):
        blog = Blog.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            blog_comment = form.save(commit=False)
            blog_comment.blog = blog
            if request.user.is_authenticated:
                blog_comment.author = request.user
            blog_comment.save()

            return  HttpResponseRedirect(blog_comment.get_absolute_url())
        return render(request, "blog/blog_detail.html", context={"form": form})


class BlogList_ajax(View):
    def get(self, request,):
        blogs = Blog.objects.all().order_by('-post_date')

        return render(request, "blog/blog_list_new.html", context={"blogs" : blogs})

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'

class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'blog/profile.html'
