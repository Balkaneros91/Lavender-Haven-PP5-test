from django.contrib import admin
from . import views
from django.urls import path
import uuid


app_name = 'testimonials'

urlpatterns = [
    path('', views.reviews_list, name='review_list'),
    path('add/', views.add_review, name='add_review'),
    path('edit/<int:pk>/', views.edit_review, name='edit_review'),
    # path('delete/<int:pk>/', views.delete_review, name='delete_review'),
]

# urlpatterns = [
#     # path('', views.testimonials_view, name="testimonials"),
#     path('leave_review/', views.leave_review, name="leave_review"),
#     path('view_review/<str:pk>', views.view_review, name="view_review"),
#     path('delete_review/<str:pk>', views.delete_review, name="delete_review"),
# ]
