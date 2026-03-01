# payments/urls.py
from django.urls import path
from .views import (
    InitiatePaymentView,
    PaymentListView,
    PaymentDetailView,
    VerifyPaymentView,
    PaymentWebhookView
)

urlpatterns = [
    path('initiate/', InitiatePaymentView.as_view(), name='initiate-payment'),
    path('', PaymentListView.as_view(), name='list-payments'),
    path('<str:reference>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('verify/', VerifyPaymentView.as_view(), name='verify-payment'),
    path('webhook/', PaymentWebhookView.as_view(), name='payment-webhook'),
]