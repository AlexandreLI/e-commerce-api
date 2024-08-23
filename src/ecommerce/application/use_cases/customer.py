from dataclasses import dataclass
from uuid import UUID

from ecommerce.domain.repositories.reservation import ReservationRepositoryInterface
from ecommerce.domain.repositories.product import ProductRepositoryInterface
from ecommerce.application.dto.customer import (
    CustomerProductReservetionOutput,
    ProductReservetionOutput,
    CustomerReservetionOutput,
)

from ecommerce.application.use_cases.exceptions import (
    ReservationNotFoundException,
)


@dataclass(frozen=True)
class ListCustomerProductsReservationUseCase:
    reservation_repository: ReservationRepositoryInterface
    product_repository: ProductRepositoryInterface

    def execute(self, customer_id: UUID) -> list[CustomerProductReservetionOutput]:
        reservations = self.reservation_repository.find_all_by_customer(customer_id)
        if not reservations:
            raise ReservationNotFoundException(customer_id)

        for reservation in reservations:
            if reservation.is_expired():
                self.reservation_repository.delete(reservation)
                self.product_repository.update(reservation.product)
                reservations.remove(reservation)

        return [
            CustomerProductReservetionOutput(
                id=reservation.id,
                reserved_at=reservation.reserved_at,
                product=ProductReservetionOutput(
                    id=reservation.product.id,
                    name=reservation.product.name,
                    status=reservation.product.status.value,
                ),
                customer=CustomerReservetionOutput(
                    id=reservation.customer.id, name=reservation.customer.name
                ),
            )
            for reservation in reservations
        ]
