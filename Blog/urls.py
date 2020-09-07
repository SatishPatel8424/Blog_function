from django.urls import path, re_path
from Blog import views
from Blog import views as Blog1
from Blog.views import SignUpView, ProfileView

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogList.as_view(), name='blogs'),

    path('blogger/<int:pk>', views.BlogListbyAuthor.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerList.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog_comment'),
    path('create-blog/', Blog1.CreateBlogView.as_view(), name="create-blog"),
    path('blogs_list/', Blog1.BlogList_ajax.as_view(), name='blogs_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]
