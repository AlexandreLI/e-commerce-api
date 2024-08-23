from dataclasses import dataclass
from uuid import UUID

from ecommerce.domain.repositories.reservation import ReservationRepositoryInterface
from ecommerce.application.dto.customer import CustomerProductReservetionOutput

from src.ecommerce.application.use_cases.exceptions import (
    ReservationNotFoundException,
)


@dataclass(frozen=True)
class ListCustomerProductsReservationUseCase:
    reservation_repository: ReservationRepositoryInterface

    def execute(self, customer_id: UUID) -> list[CustomerProductReservetionOutput]:
        reservations = self.reservation_repository.find_all_by_customer(customer_id)
        if not reservations:
            raise ReservationNotFoundException(customer_id)

        return [
            CustomerProductReservetionOutput(
                product_id=reservation.product.id,
                product_name=reservation.product.name,
            )
            for reservation in reservations
        ]
