from pydoc import pager

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article


def articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()

    paginator = Paginator(articles, 5)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'page_obj': page_obj
    }
    if request.htmx:
        return render(request, 'partials/articles_category.html', context)
    return render(request, 'pages/articles_category.html', context)


def navbar(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'navbar_options.html', context)


def mobile_navbar(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'mobile_navbar_options.html', context)


def home(request):
    last_articles = Article.objects.all().order_by('-created_at')[:5]
    context = {
        'articles': last_articles
    }
    if request.htmx:
        return render(request, 'partials/home.html', context)
    return render(request, 'pages/home.html', context)


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {
        'article': article
    }
    if request.htmx:
        return render(request, 'partials/article_detail.html', context)
    return render(request, 'pages/article_detail.html', context)
