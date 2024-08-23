import pytest
from uuid import UUID
import datetime

from ecommerce.application.use_cases.customer import (
    ListCustomerProductsReservationUseCase,
)
from ecommerce.infra.repositories.in_memory_reservation import (
    InMemoryReservationRepository,
)
from ecommerce.infra.repositories.in_memory_product import (
    InMemoryProductRepository,
)
from ecommerce.domain.entities.reservation import Reservation
from ecommerce.domain.entities.product import Product, StatusEnum
from ecommerce.domain.entities.customer import Customer
from ecommerce.application.use_cases.exceptions import ReservationNotFoundException

from tests.ecommerce.mock_data import reservations, products


def test_list_customer_reservation_product():

    reservation_repository = InMemoryReservationRepository(reservations=reservations)

    product_repository = InMemoryProductRepository(products=products)
    use_case = ListCustomerProductsReservationUseCase(
        reservation_repository=reservation_repository,
        product_repository=product_repository,
    )

    result = use_case.execute(customer_id=reservations[0].customer.id)

    assert len(result) == 1
    assert result[0].product.name == reservations[0].product.name


def test_list_customer_reservation_product_not_found():

    reservation_repository = InMemoryReservationRepository(reservations=reservations)
    product_repository = InMemoryProductRepository(products=products)

    use_case = ListCustomerProductsReservationUseCase(
        reservation_repository=reservation_repository,
        product_repository=product_repository,
    )

    with pytest.raises(ReservationNotFoundException):
        use_case.execute(customer_id=UUID("123e4567-e89b-12d3-a456-426614174000"))


def test_list_customer_reservation_expired():
    product = Product(name="Product 1", status=StatusEnum.AVAILABLE)

    reservation = Reservation(
        customer=Customer(name="John Doe"),
        product=product,
        reserved_at=datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=4),
    )

    reservation_repository = InMemoryReservationRepository(reservations=[reservation])
    product_repository = InMemoryProductRepository(products=[product])

    use_case = ListCustomerProductsReservationUseCase(
        reservation_repository=reservation_repository,
        product_repository=product_repository,
    )

    result = use_case.execute(customer_id=reservation.customer.id)

    assert len(result) == 0
    assert result == []
