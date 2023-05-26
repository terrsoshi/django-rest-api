from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from . import api_views

urlpatterns = [
    path('api/v1/products/', api_views.ProductList.as_view(), name='list-product-API'),
    path('api/v1/products/new', api_views.ProductCreate.as_view(), name='create-product-API'),
    path('api/v1/products/<int:id>/', api_views.ProductRetrieveUpdateDestroy.as_view(), name='retrieve-update-destroy-product-API'),
    path('api/v1/products/<int:id>/stats', api_views.ProductStats.as_view(), name='stats-product-API'),
    path('products/<int:id>/', views.ShowView.as_view(), name='show-product'),
    path('cart/', views.CartView.as_view(), name='shopping-cart'),
    path('', views.IndexView.as_view(), name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
