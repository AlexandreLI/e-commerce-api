import pytest
import datetime

from ecommerce.application.use_cases.product import (
    ListProductUseCase,
)
from ecommerce.infra.repositories.in_memory_product import (
    InMemoryProductRepository,
)
from ecommerce.infra.repositories.in_memory_reservation import (
    InMemoryReservationRepository,
)
from ecommerce.domain.entities.reservation import Reservation
from ecommerce.domain.entities.product import Product
from ecommerce.application.dto.product import ProductOutput
from ecommerce.domain.entities.product import StatusEnum
from tests.ecommerce.mock_data import products, customers


@pytest.fixture
def reservations() -> list[Reservation]:
    reservation_1 = Reservation(
        customer=customers[0],
        product=products[0],
    )

    reservation_2 = Reservation(
        customer=customers[1],
        product=products[1],
        reserved_at=datetime.datetime.now() - datetime.timedelta(days=4),
    )
    return [reservation_1, reservation_2]


def test_list_products_use_case(reservations):
    product_repo = InMemoryProductRepository(products)

    reservation_repo = InMemoryReservationRepository(
        reservations=reservations, products=products, customers=customers
    )
    use_case = ListProductUseCase(
        product_repo=product_repo, reservation_repo=reservation_repo
    )

    expected_result = [
        ProductOutput(
            id=products[0].id,
            name="Product 1",
            status=StatusEnum.AVAILABLE,
        ),
        ProductOutput(
            id=products[1].id,
            name="Product 2",
            status=StatusEnum.AVAILABLE,
        ),
        ProductOutput(
            id=products[2].id,
            name="Product 3",
            status=StatusEnum.RESERVED,
        ),
        ProductOutput(
            id=products[3].id,
            name="Product 4",
            status=StatusEnum.UNAVAILABLE,
        ),
    ]
    result = use_case.execute()

    assert len(result) == 4
    assert result == expected_result
    assert isinstance(result, list)
    assert isinstance(result[0], ProductOutput)


def test_list_products_use_case_empty():
    product_repo = InMemoryProductRepository([])

    repository = InMemoryReservationRepository([])
    use_case = ListProductUseCase(
        reservation_repo=repository, product_repo=product_repo
    )

    result = use_case.execute()

    assert len(result) == 0
    assert result == []
    assert isinstance(result, list)
