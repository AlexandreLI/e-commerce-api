from django.urls import path

from .views import ListCustomerReservedProductsView

urlpatterns = [
    path("", ListCustomerReservedProductsView.as_view(), name="list_customers"),
]
