from uuid import uuid4
from django.db import models
from django_project.customer.models import Customer
from django_project.product.models import Product


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
