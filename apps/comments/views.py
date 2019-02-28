from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View

from blog.models import Article
from .models import Comment
from .forms import CommentForm

# Create your views here.

class ArticleConmmetsView(View):
    def get(self,request,article_id):
        articles = Article.objects.get(id=int(article_id))
        all_comments = Comment.objects.all()
        return render(request, 'detail.html')


# def post_comment(request,post_pk):
#     post = get_object_or_404(Article,pk=post_pk)
#     if request.method =='POST':
#         form = CommentForm(request.POST)
#
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect(post)
#
#         else:
#             comment_list = post.comment_set.all()
#             context = {'post':post,
#                        'form':form,
#                        'comment_list':comment_list}
#             return render (request,'detail.html',context=context)
#     return redirect(post)
