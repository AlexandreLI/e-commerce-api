import pytest

from ecommerce.domain.entities.reservation import Reservation
from ecommerce.domain.entities.product import Product, StatusEnum
from ecommerce.domain.entities.customer import Customer
from django_project.reservation.models import Reservation as ReservationModel
from django_project.product.models import Product as ProductModel
from django_project.customer.models import Customer as CustomerModel
from django_project.reservation.repository import DjangoReservationRepository


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
