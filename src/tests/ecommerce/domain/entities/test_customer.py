import pytest
from ecommerce.domain.entities.customer import Customer


def test_customer_can_be_created():
    customer = Customer(name="John Doe")

    assert isinstance(customer, Customer)
    assert customer.name == "John Doe"
    assert customer.id is not None


def test_customer_name_cannot_be_empty():
    with pytest.raises(ValueError):
        Customer(name="")


def test_customer_name_cannot_be_longer_than_255_characters():
    with pytest.raises(ValueError):
        Customer(name="a" * 256)
