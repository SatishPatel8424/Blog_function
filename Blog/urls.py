from django.urls import path
from  .import views
from django.conf.urls import url

urlpatterns = [
   path("", views.index, name="index"),
   path("blogs/", views.BlogList, name="BlogList"),
   url(r'^blog/(?P<pk>[\d]+)/$', views.BlogDetail.as_view(), name='blog-detail'),
   url(r'bloggers/$', views.BlogAuthorList.as_view(), name='bloggers'),
]
