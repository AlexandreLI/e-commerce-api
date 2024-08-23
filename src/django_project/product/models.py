from uuid import uuid4
from django.db import models


class Product(models.Model):
    class StatusEnum(models.TextChoices):
        AVAILABLE = "AVAILABLE"
        UNAVAILABLE = "UNAVAILABLE"
        RESERVED = "RESERVED"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=11,
        choices=StatusEnum.choices,
    )
