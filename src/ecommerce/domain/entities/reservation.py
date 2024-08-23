from dataclasses import dataclass, field
from uuid import UUID, uuid4
import datetime

from ecommerce.domain.entities.product import Product, StatusEnum
from ecommerce.domain.entities.customer import Customer


@dataclass
class Reservation:
    product: Product
    customer: Customer
    reserved_at: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    id: UUID = field(default_factory=uuid4)

    def validate_product_availability(self) -> ValueError | None:
        if self.product.status is not StatusEnum.AVAILABLE:
            raise ValueError("Product unavailable or already reserved")

    def is_expired(self) -> bool:
        diference = datetime.datetime.now(datetime.timezone.utc) - self.reserved_at
        return diference.days > 3
