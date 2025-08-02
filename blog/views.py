from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article


def articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        'category': category,
        'articles': category.articles.all()
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
    if request.htmx:
        return render(request, 'partials/home.html')
    return render(request, 'pages/home.html')


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {
        'article': article
    }
    if request.htmx:
        return render(request, 'partials/article_detail.html', context)
    return render(request, 'pages/article_detail.html', context)
