from pydoc import pager

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from blog.models import Category, Article, Comment


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


def search_articles(request):
    query = request.GET.get('q', '')
    articles = []
    
    if query:
        articles = Article.objects.filter(
            title__icontains=query
        ).order_by('-created_at')[:10]
    
    context = {
        'articles': articles,
        'query': query
    }
    
    if request.htmx:
        return render(request, 'partials/search_results.html', context)
    return render(request, 'pages/search.html', context)


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()[:10]  # Show latest 10 comments
    
    context = {
        'article': article,
        'comments': comments
    }
    if request.htmx:
        return render(request, 'partials/article_detail.html', context)
    return render(request, 'pages/article_detail.html', context)


def add_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        author_name = request.POST.get('author_name', '').strip()
        content = request.POST.get('content', '').strip()
        
        if author_name and content:
            comment = Comment.objects.create(
                article=article,
                author_name=author_name,
                content=content
            )
            
            if request.htmx:
                # Return the updated comments list
                comments = article.comments.all()[:10]
                context = {'comments': comments}
                return render(request, 'partials/comments_list.html', context)
        else:
            if request.htmx:
                return render(request, 'partials/comment_form.html', {
                    'article': article,
                    'error': 'Please fill in all fields.'
                })
    
    if request.htmx:
        return render(request, 'partials/comment_form.html', {'article': article})
    
    return redirect('article-detail', id=article_id)
