from django.urls import path
from django_project.reservation.views import ReserveProductView


urlpatterns = [
    path("", ReserveProductView.as_view(), name="reserve_product"),
]
