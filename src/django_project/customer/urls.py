from django.urls import path

from .views import ListCustomerReservedProductsView

urlpatterns = [
    path(
        "<uuid:customer_id>/reservations",
        ListCustomerReservedProductsView.as_view(),
        name="list_customer_reservations",
    ),
]
