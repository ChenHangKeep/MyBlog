from django.shortcuts import render, HttpResponse
from django.views.generic import View
from blog.models import Article
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from .models import Comment
from .forms import CommentForm
# Create your views here.


#显示评论
class ArticleConmmetsView(View):
    def get(self,request,article_id):
        all_comments = Comment.objects.filter(article=article_id)
        return render(request, 'detail.html',{
            "all_comments": all_comments
        })


class AddCommentView(View):

    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type='application/json')
#
#     # def post(self, request):
#     #     article_id = request.POST.get("article_id")
#     #     comments = request.POST.get('comments', '')
#     # # if article_id>0 and comments:
#     #     comments=Comment()
#     #     article =Article.objects.get(id=int(article_id))
#     #     comments.course = article
#     #     comments.conmments = comments
#     #     comments.user = request.user
#     #     comments.save()



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

