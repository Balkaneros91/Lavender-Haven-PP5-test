from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.items_view, name='items'),
    path('', views.all_products, name='items'),
    # path('<int:product_id>/', views.product_detail, name='items_detailed'),
    # path('add/', views.add_product, name='add_item'),
    # path('edit/<int:product_id>/', views.edit_product, name='edit_itemt'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_item'),  # noqa
]
