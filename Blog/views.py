from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Blog,BlogAuthor
from django.views import View


# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )

def BlogList(request):

    blog = Blog.objects.all()
    most_recent = Blog.objects.order_by('-timestamp')[:3]
    Paginatora1 = Paginator(BlogList,5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    """"
    try:
        paginated_queryset = Paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = Paginator.page(page)
    except EmptyPage:
        paginated_queryset = Paginator.page(Paginator.num_pages)

"""
    context = {
        #'queryset': paginated_queryset,
        'page_request_var' : page_request_var,
        'blog': blog,
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


class BlogAuthorList(View):
    def get(self, request):
        BlogAuthor1 = BlogAuthor.objects.all()
        return render(request, 'blog/blogauthor_list.html', {'BlogAuthor1': BlogAuthor1})

