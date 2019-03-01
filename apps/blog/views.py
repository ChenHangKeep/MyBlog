import pygments
import markdown
from pure_pagination import PageNotAnInteger, Paginator

from django.shortcuts import render,get_object_or_404
from django.views.generic import View

from .models import Article,Category
from comments.models import Comment

# Create your views here.


#首页
class IndexView(View):
    def get(self, request):
        #取出文章，并按照添加时间排序
        article_list = Article.objects.all().order_by("-add_time")

        #最新文章，取前三个
        newest_article = Article.objects.all().order_by("-add_time")[:3]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(article_list, 5, request=request)
        articles = p.page(page)

        return render(request,'index.html',{
            'article_list': articles,
            'newest_article': newest_article
        })


class DetailView(View):
    def get(self, request,article_id):
        article = Article.objects.get(id=int(article_id))

        newest_article = Article.objects.all().order_by("-add_time")[:3]

        #增加阅读数
        article.views +=1
        article.save()

        article.content = markdown.markdown(article.content,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return render(request, 'detail.html', {
            'article':article,
            'newest_article':newest_article
        })




class ArchivesView(View):
    def get(self, request, year, month):
        all_article = Article.objects.filter(
            add_time__year=year,
            add_time__month=month
        )
        dates = Article.objects.datetimes('add_time', 'month', order='DESC')
        return render(request, "index.html", {
            "all_article": all_article,
            'dates': dates
       })


class CategoryView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=int(category_id))

        #统计类别个数
        category_count = Category.objects.all().count()

        category_article = Article.objects.filter(category_id=category).order_by("-add_time")
        return render(request,"index.html",{
            'category_article':category_article,
            'category_count':category_count
        })



# def category(request, pk):
#      # 记得在开始部分导入 Category 类
#      cate = get_object_or_404(Category, pk=pk)
#      post_list = Article.objects.filter(category=cate).order_by('-add_time')
#      return render(request, 'index.html', context={'post_list': post_list})

