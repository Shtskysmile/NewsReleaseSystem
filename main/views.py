from django.shortcuts import render
from django.core.paginator import Paginator
from article.models import ArticleInfo, Category
from django.db.models import Q

def index(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    if query:
        article_list = ArticleInfo.objects.filter(
            Q(title__icontains=query) | Q(desc__icontains=query) | Q(content__icontains=query)
        )
    elif category_id:
        article_list = ArticleInfo.objects.filter(category_id=category_id)
    else:
        article_list = ArticleInfo.objects.all()

    paginator = Paginator(article_list, 9)  # 每页显示4篇文章
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'index.html',
                  {'page_obj': page_obj, 'categories': categories, 'query': query, 'category_id': category_id})