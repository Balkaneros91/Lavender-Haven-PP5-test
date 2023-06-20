from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.blog_view, name='blog'),
    path('', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('like/<slug:slug>', views.BlogLike.as_view(), name='blog_like')
]
