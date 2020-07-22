from django.urls import path, re_path
from Blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogList.as_view(), name='blogs'),
    path('blogs/create', views.CreateBlogView.as_view(), name="create-blog"),
    path('blogger/<int:pk>', views.BlogListbyAuthor.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerList.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment/', views.BlogDetail.as_view(), name='blog_comment'),
]
