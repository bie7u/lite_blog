from django.urls import path
from blog import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('articles/<slug:slug>/', views.articles, name='articles'),
    path('navbar/', views.navbar, name='navbar'),
    path('mobile-navbar/', views.mobile_navbar, name='mobile-navbar'),
    path('', views.home, name='home'),
    path('article-detail/<int:id>/', views.article_detail, name='article-detail'),
]
