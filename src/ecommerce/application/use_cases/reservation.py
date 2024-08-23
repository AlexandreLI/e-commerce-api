from dataclasses import dataclass
from uuid import UUID

from ecommerce.domain.repositories.reservation import ReservationRepositoryInterface
from ecommerce.domain.repositories.product import ProductRepositoryInterface
from ecommerce.domain.repositories.customer import CustomerRepositoryInterface
from ecommerce.domain.entities.product import StatusEnum
from ecommerce.domain.entities.reservation import Reservation
from src.ecommerce.application.use_cases.exceptions import (
    NotFoundException,
    InvalidReservationException,
)
from ecommerce.application.dto.reservation import ReservationOutput


@dataclass(frozen=True)
class CreateReservationUseCase:
    reservation_repo: ReservationRepositoryInterface
    product_repo: ProductRepositoryInterface
    customer_repo: CustomerRepositoryInterface

    @dataclass
    class InputParams:
        customer_id: UUID
        product_id: UUID

    def execute(self, input_params: InputParams) -> ReservationOutput:
        customer = self.customer_repo.get_by_id(input_params.customer_id)
        if customer is None:
            raise NotFoundException(input_params.customer_id, "Customer")

        product = self.product_repo.get_by_id(input_params.product_id)
        if product is None:
            raise NotFoundException(input_params.product_id, "Product")

        try:
            reservation_entity = Reservation(customer=customer, product=product)
        except (ValueError, KeyError) as error:
            raise InvalidReservationException(error) from error

        reservation = self.reservation_repo.create(entity=reservation_entity)

        product.update_status(StatusEnum.RESERVED)
        self.product_repo.update(entity=product)

        return ReservationOutput(
            product_id=reservation.product.id,
            customer_id=reservation.customer.id,
            reserved_at=reservation.reserved_at,
            id=reservation.id,
        )
