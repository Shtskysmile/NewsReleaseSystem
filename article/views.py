from django.shortcuts import render, redirect
from user.views import logout
from .models import ArticleInfo
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def article_read(request, aid):
    article = get_object_or_404(ArticleInfo, id=aid)
    previous_article = ArticleInfo.objects.filter(id__lt=article.id).order_by('-id').first()
    next_article = ArticleInfo.objects.filter(id__gt=article.id).order_by('id').first()
    return render(request, 'article/read.html', {
        'article': article,
        'previous_article': previous_article,
        'next_article': next_article
    })

@login_required(login_url='/user/login/')
def article_edit(request, aid):
    article = ArticleInfo.objects.get(id=aid)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)  # 添加 request.FILES
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('article:read', aid=aid)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article/edit.html', {'form': form})

@login_required(login_url='/user/login/')
def article_delete(request, aid):
    article = ArticleInfo.objects.get(id=aid)
    article.delete()
    return redirect('article:list')

@login_required(login_url='/user/login/')
def article_write(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # 添加 request.FILES
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = ArticleForm()
    return render(request, 'article/write.html', {'form': form})

@login_required(login_url='/user/login/')
def article_list(request):
    articles = ArticleInfo.objects.all().filter(author=request.user)
    return render(request, 'article/list.html', {'articles': articles})