import pytest
from uuid import UUID

from ecommerce.application.use_cases.customer import (
    ListCustomerProductsReservationUseCase,
)
from ecommerce.infra.repositories.in_memory_reservation import (
    InMemoryReservationRepository,
)
from src.ecommerce.application.use_cases.exceptions import ReservationNotFoundException

from tests.ecommerce.mock_data import reservations


def test_list_customer_reservation_product():

    reservation_repository = InMemoryReservationRepository(reservations=reservations)

    use_case = ListCustomerProductsReservationUseCase(
        reservation_repository=reservation_repository
    )

    result = use_case.execute(customer_id=reservations[0].customer.id)

    assert len(result) == 1
    assert result[0].product_name == reservations[0].product.name


def test_list_customer_reservation_product_not_found():

    reservation_repository = InMemoryReservationRepository(reservations=reservations)

    use_case = ListCustomerProductsReservationUseCase(
        reservation_repository=reservation_repository
    )

    with pytest.raises(ReservationNotFoundException):
        use_case.execute(customer_id=UUID("123e4567-e89b-12d3-a456-426614174000"))
