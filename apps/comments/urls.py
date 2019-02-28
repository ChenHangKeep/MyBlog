from django.conf.urls import url
from .views import ArticleConmmetsView
app_name='comments'

urlpatterns = [
    url(r'^comment/article/(?P<post_pk>[0-9]+)/$',ArticleConmmetsView.as_view(),name='article_comment'),
]