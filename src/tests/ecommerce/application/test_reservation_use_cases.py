import pytest
from uuid import UUID

from ecommerce.application.use_cases.reservation import (
    CreateReservationUseCase,
)
from ecommerce.infra.repositories.in_memory_reservation import (
    InMemoryReservationRepository,
)
from ecommerce.infra.repositories.in_memory_product import (
    InMemoryProductRepository,
)
from ecommerce.infra.repositories.in_memory_customer import (
    InMemoryCustomerRepository,
)
from ecommerce.domain.entities.product import StatusEnum, Product
from ecommerce.application.dto.reservation import ReservationOutput
from tests.ecommerce.mock_data import products, customers


def test_create_reservation_use_case():
    reservation_repo = InMemoryReservationRepository(
        reservations=[], products=products, customers=customers
    )
    product_repo = InMemoryProductRepository(products=products)
    customer_repo = InMemoryCustomerRepository(customers=customers)
    
    use_case = CreateReservationUseCase(
        reservation_repo=reservation_repo,
        product_repo=product_repo,
        customer_repo=customer_repo,
    )
    input_params = CreateReservationUseCase.InputParams(
        customer_id=customers[0].id, product_id=products[0].id
    )
    result = use_case.execute(input_params)

    assert isinstance(result, ReservationOutput)
    assert result.product_id == products[0].id


def test_create_reservation_use_case_unavailable():
    reservation_repo = InMemoryReservationRepository(
        reservations=[], products=products, customers=customers
    )
    product_repo = InMemoryProductRepository(products=products)
    customer_repo = InMemoryCustomerRepository(customers=customers)
    use_case = CreateReservationUseCase(
        reservation_repo=reservation_repo,
        product_repo=product_repo,
        customer_repo=customer_repo,
    )
    input_params = CreateReservationUseCase.InputParams(
        customer_id=customers[0].id, product_id=products[2].id
    )
    with pytest.raises(Exception, match="Product unavailable or already reserved"):
        use_case.execute(input_params)


def test_create_reservation_use_case_reserved_product():
    reservation_repo = InMemoryReservationRepository(
        reservations=[], products=products, customers=customers
    )
    product_repo = InMemoryProductRepository(products=products)
    customer_repo = InMemoryCustomerRepository(customers=customers)
    use_case = CreateReservationUseCase(
        reservation_repo=reservation_repo,
        product_repo=product_repo,
        customer_repo=customer_repo,
    )
    input_params = CreateReservationUseCase.InputParams(
        customer_id=customers[0].id,
        product_id=products[3].id,
    )
    with pytest.raises(Exception, match="Product unavailable or already reserved"):
        use_case.execute(input_params)


def test_create_reservation_use_case_not_found():
    product = Product(name="Product 1", status=StatusEnum.AVAILABLE)
    reservation_repo = InMemoryReservationRepository(
        reservations=[],
        products=[product],
        customers=customers,
    )
    product_repo = InMemoryProductRepository(products=products)
    customer_repo = InMemoryCustomerRepository(customers=customers)
    use_case = CreateReservationUseCase(
        reservation_repo=reservation_repo,
        product_repo=product_repo,
        customer_repo=customer_repo,
    )
    input_params = CreateReservationUseCase.InputParams(
        customer_id=UUID("00000000-0000-0000-0000-000000000000"),
        product_id=product.id,
    )
    with pytest.raises(
        Exception,
        match="Customer with id 00000000-0000-0000-0000-000000000000 not found",
    ):
        use_case.execute(input_params)


def test_create_reservation_use_case_not_found_product():
    reservation_repo = InMemoryReservationRepository(
        reservations=[], products=products, customers=customers
    )
    product_repo = InMemoryProductRepository(products=products)
    customer_repo = InMemoryCustomerRepository(customers=customers)
    use_case = CreateReservationUseCase(
        reservation_repo=reservation_repo,
        product_repo=product_repo,
        customer_repo=customer_repo,
    )
    input_params = CreateReservationUseCase.InputParams(
        customer_id=customers[0].id,
        product_id=UUID("00000000-0000-0000-0000-000000000000"),
    )
    with pytest.raises(
        Exception,
        match="Product with id 00000000-0000-0000-0000-000000000000 not found",
    ):
        use_case.execute(input_params)
