from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.serializers import json
from django.http import HttpResponseRedirect, JsonResponse, Http404, HttpResponse, request
from django.shortcuts import render, redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from Blog.forms import CreateBlogForm,ProfileForm,SignUpForm
from .models import Blog, BlogUsers, BlogComment
from django.views import View, generic


# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
    )


class BlogList(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            blogs = Blog.objects.all().order_by('-post_date')
            blog_list = serializers.serialize('json', blogs)
            return JsonResponse(blog_list, safe=False)


        else:
            user = request.user
           # bio = BlogUsers.objects.get(bio='bio')
            blogger = BlogUsers.objects.get(user=user)
            blogs = Blog.objects.filter(author=blogger).order_by('-post_date')
            blog_list1 = serializers.serialize('json', blogs)
            return JsonResponse(blog_list1, safe=False)




class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'


class BloggerList(generic.ListView):
    model = BlogUsers
    template_name = 'blog/blogauthor_list.html'
    queryset = BlogUsers.objects.all()




class BlogListbyAuthor(generic.ListView):
    model = Blog
    paginate_by = 5
    template_name = 'blog/blog_list_by_author.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_author = get_object_or_404(BlogUsers, pk=id)
        return Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        context = super(BlogListbyAuthor, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogUsers, pk=self.kwargs['pk'])
        return context


class CreateBlogView(generic.FormView):
    form_class = CreateBlogForm
    template_name = "blog/create_blog.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        return render(self.request, self.template_name, {"form": form})

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        buser=BlogUsers.objects.get(user=self.request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = buser
            post.save()
            return JsonResponse({"success": True}, status=200)

        return JsonResponse({"success": False, "errors": form.errors}, status=400)


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ["description", ]
    template_name = 'blog/blogcomment_form.html'

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })

class BlogList_ajax(generic.ListView):
    model = Blog
    paginate_by = 5
    template_name = 'blog/blog_list_new.html'
    ordering = ['-post_date']

    def get_queryset(self):

        return Blog.objects.all()



class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('blog')
    template_name = 'blog/signup.html'


    def form_valid(self, form):
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], )
        login(self.request, user)
        return HttpResponseRedirect(reverse('blogs_list'))


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('index')
    template_name = 'blog/profile.html'
