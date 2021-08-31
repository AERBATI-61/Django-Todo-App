from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def indexview(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        context = {
            'articles': articles,
            'keyword': keyword
        }
        return render(request, 'articles.html', context)

    return render(request, 'index.html')

    # context = {
    #     'n': 10,
    #     'm': 20,
    #     'list': [1,2,3,4,5,6,7]
    # }
    # return render(request, 'index.html', context)

def articlesview(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, 'articles.html', {"articles": articles})
    articles = Article.objects.all()
    return render(request, 'articles.html', {"articles":articles})



def aboutview(request):
    return render(request, 'about.html')


@login_required(login_url="user:login")
def dashbordview(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return  render(request, 'dashbord.html', context)




@login_required(login_url="user:login")
def addarticleview(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Basariyla olusturuldu")
        return redirect('article:dashbord')

    return  render(request, 'addarticle.html', {"form": form})

def detailview(request, id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id = id)
    comments = article.comments.all()[:3]
    return render(request, 'detail.html', {"article": article, "comments": comments})

@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Basariyla Guncellendi")
        return redirect('article:dashbord')
    return render(request, 'update.html', {"form":form})

@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Makale Basariyla Silindi")
    return redirect('article:dashbord')

# def detailview(request, id):
#     return HttpResponse("Detail sayfasi Id = " + str(id))


def addComment(request, id):
    article = get_object_or_404(Article, id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()
        return redirect(reverse('article:detail', kwargs={'id':id}))