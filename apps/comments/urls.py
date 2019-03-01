from django.conf.urls import url
from .views import ArticleConmmetsView, AddCommentView
app_name='comments'

urlpatterns = [
    url(r'^comment/(?P<article_id>[0-9]+)/$', ArticleConmmetsView.as_view(), name='article_comment'),
    url(r'^add_comment/$',AddCommentView.as_view(), name='add_comment'),
]