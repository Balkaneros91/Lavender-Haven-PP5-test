from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.subscription_view, name='subscription'),
    path('', views.newsletter, name='newsletter'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
]
