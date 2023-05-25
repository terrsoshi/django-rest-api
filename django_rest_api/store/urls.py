from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('products/<int:pk>/', views.ShowView.as_view(), name='show-product'),
    path('cart/', views.CartView.as_view(), name='shopping-cart'),
    path('', views.IndexView.as_view(), name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
