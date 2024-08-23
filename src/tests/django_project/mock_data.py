import pytest
import datetime

from ecommerce.domain.entities.reservation import Reservation
from ecommerce.domain.entities.product import Product, StatusEnum
from ecommerce.domain.entities.customer import Customer
from django_project.reservation.models import Reservation as ReservationModel
from django_project.product.models import Product as ProductModel
from django_project.customer.models import Customer as CustomerModel
from django_project.reservation.repository import DjangoReservationRepository


@pytest.fixture
def product_entity_unavailable() -> Product:
    return Product(name="Product 1", status=StatusEnum.UNAVAILABLE)


@pytest.fixture
def product_entity_reserved() -> Product:
    return Product(name="Product 1", status=StatusEnum.RESERVED)


@pytest.fixture
def product_entity() -> Product:
    return Product(name="Product 1", status=StatusEnum.AVAILABLE)


@pytest.fixture
def customer_entity() -> Customer:
    return Customer(name="John Doe")


@pytest.fixture
def product_model(product_entity: Product) -> ProductModel:
    return ProductModel.objects.create(
        id=product_entity.id,
        name=product_entity.name,
        status=product_entity.status.value,
    )


@pytest.fixture
def customer_model(customer_entity: Customer) -> CustomerModel:
    return CustomerModel.objects.create(
        id=customer_entity.id,
        name="John Doe",
    )


@pytest.fixture
def product_model_unavailable(product_entity_unavailable: Product) -> ProductModel:
    return ProductModel.objects.create(
        id=product_entity_unavailable.id,
        name=product_entity_unavailable.name,
        status=product_entity_unavailable.status.value,
    )


@pytest.fixture
def product_model_reserved(product_entity_reserved: Product) -> ProductModel:
    return ProductModel.objects.create(
        id=product_entity_reserved.id,
        name=product_entity_reserved.name,
        status=product_entity_reserved.status.value,
    )


@pytest.fixture
def reservation_entity(
    product_entity: Product, customer_entity: Customer
) -> Reservation:
    return Reservation(
        product=product_entity,
        customer=customer_entity,
    )


@pytest.fixture
def reservation_model(
    reservation_entity: Reservation,
) -> ReservationModel:
    return ReservationModel.objects.create(
        id=reservation_entity.id,
        product_id=reservation_entity.product.id,
        customer_id=reservation_entity.customer.id,
        reservation_date=datetime.datetime.now(datetime.timezone.utc),
    )
