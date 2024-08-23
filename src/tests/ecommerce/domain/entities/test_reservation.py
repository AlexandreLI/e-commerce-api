import pytest
import datetime

from ecommerce.domain.entities.product import Product, StatusEnum
from ecommerce.domain.entities.customer import Customer
from ecommerce.domain.entities.reservation import Reservation


@pytest.fixture
def customer() -> Customer:
    return Customer(name="John Doe")


def test_reservation_can_be_created(customer: Customer):
    reservation = Reservation(
        customer=customer,
        product=Product(name="Product 1", status=StatusEnum.AVAILABLE),
    )

    assert isinstance(reservation, Reservation)
    assert isinstance(reservation.customer, Customer)
    assert isinstance(reservation.product, Product)
    assert reservation.id is not None


def test_reservation_product_is_not_available(customer: Customer):
    with pytest.raises(ValueError, match="Product unavailable or already reserved"):
        Reservation(
            customer=customer,
            product=Product(name="Product 2", status=StatusEnum.UNAVAILABLE),
            reserved_at=datetime.datetime.now(),
        )


def test_reservation_product_is_reserved(customer: Customer):
    with pytest.raises(ValueError, match="Product unavailable or already reserved"):
        Reservation(
            customer=customer,
            product=Product(name="Product 3", status=StatusEnum.RESERVED),
            reserved_at=datetime.datetime.now(),
        )


def test_reservation_is_expired_true(customer: Customer):
    reservation = Reservation(
        customer=customer,
        product=Product(name="Product 4", status=StatusEnum.AVAILABLE),
        reserved_at=datetime.datetime.now() - datetime.timedelta(days=4),
    )
    result = reservation.is_expired()

    assert result is True


def test_reservation_is_expired_false(customer: Customer):
    reservation = Reservation(
        customer=customer,
        product=Product(name="Product 4", status=StatusEnum.AVAILABLE),
        reserved_at=datetime.datetime.now() - datetime.timedelta(days=3),
    )
    result = reservation.is_expired()

    assert result is False
