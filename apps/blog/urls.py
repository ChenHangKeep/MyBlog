from django.conf.urls import url
from .views import IndexView,DetailView, ArchivesView, CategoryView

app_name ='blog'

urlpatterns =[
   url(r'^$', IndexView.as_view(),name='index'),
   url(r'^article/(?P<article_id>\d+)/$',DetailView.as_view(),name='article_detail'),
   url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(),name='archives'),
   url(r'^category/(?P<category_id>[0-9]+)/$',CategoryView.as_view(),name='category'),

]
