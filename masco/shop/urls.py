from django.urls import path
from .views import (
    CategoryListView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ReviewCreateView,
    CartListView,
    CartCreateView,
    CartDeleteView,
    EnquiryCreateView,
    OrderCreateView,  # ✅ Added
)

urlpatterns = [
    # ----------------------------
    # Categories
    # ----------------------------
    path('categories/', CategoryListView.as_view(), name='category-list'),

    # ----------------------------
    # Products
    # ----------------------------
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    # path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    # path('products/create/', ProductCreateView.as_view(), name='product-create'),

    # ----------------------------
    # Reviews
    # ----------------------------
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),

    # ----------------------------
    # Cart
    # ----------------------------
    path('cart/', CartListView.as_view(), name='cart-list'),
    path('cart/add/', CartCreateView.as_view(), name='cart-add'),
    path('cart/remove/<int:pk>/', CartDeleteView.as_view(), name='cart-remove'),

    # ----------------------------
    # Enquiries
    # ----------------------------
    path('enquiries/create/', EnquiryCreateView.as_view(), name='enquiry-create'),

       # ... other API paths
    path("orders/", OrderCreateView.as_view(), name="order-create"),
]
