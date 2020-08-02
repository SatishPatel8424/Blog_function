from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from Blog.forms import CreateBlogForm,CommentForm
from .models import Blog,BlogAuthor
from django.views import View


# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )

class BlogList(View):
    def get(self, request):
        blogs = Blog.objects.all().order_by('-post_date')
        most_recent = blogs[:3]
        page_request_var = 'page'

        context = {
                'blogs' : blogs,
                'page_request_var' : page_request_var,
                'most_recent': most_recent,

        }
        return render(request, "blog/blog_list.html", context)


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
        BlogAuthor1 = BlogAuthor.objects.all()
        return render(request, 'blog/blogauthor_list.html', {'BlogAuthor1': BlogAuthor1})



class BlogListbyAuthor(View):
    def get(self, request,pk):

        blogger = BlogAuthor.objects.get(pk=pk) #Bloger
        blogs = Blog.objects.filter(author=blogger)
        context = {'blog_author': blogger,
                   'blogs': blogs}

        return render(request, "blog/blog_list_by_author.html", context)


class CreateBlogView(View):

    def get(self, request):
        blog_form = CreateBlogForm()
        return render(request, "blog/create_blog.html", context={"form" : blog_form})

    def post(self, request):
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            print(blog.get_absolute_url())
            return HttpResponseRedirect(blog.get_absolute_url())
        return render(request, "blog/create_blog.html", context={"form" : form})


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



