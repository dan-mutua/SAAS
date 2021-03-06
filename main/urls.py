from django.urls import path
from djangoflutterwave.views import (
    TransactionCreateView,
    TransactionDetailView,
    PaymentParamsView,
)


app_name = "djangoflutterwave"

urlpatterns = [
    path("transaction/", TransactionCreateView.as_view(), name="transaction_create"),
    path("payment-params/", PaymentParamsView.as_view(), name="payment_params"),
    path("<str:tx_ref>/", TransactionDetailView.as_view(), name="transaction_detail"),
]