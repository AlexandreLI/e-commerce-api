import pytest
from ecommerce.domain.entities.product import Product, StatusEnum


def test_product_can_be_created():
    product = Product(name="Product 1", status=StatusEnum.AVAILABLE)

    assert isinstance(product, Product)
    assert product.name == "Product 1"
    assert product.id is not None


def test_product_with_wrong_status():
    with pytest.raises(
        ValueError, match="Invalid status 'wrong_status'. Must be one of: .*"
    ):
        Product(name="Product 1", status="wrong_status")


def test_update_product_status():
    product = Product(name="Product 1", status=StatusEnum.AVAILABLE)
    product.update_status(StatusEnum.RESERVED)

    assert product.status == StatusEnum.RESERVED


def test_product_name_cannot_be_empty():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Product(name="", status=StatusEnum.AVAILABLE)


def test_product_name_cannot_be_longer_than_255_characters():
    with pytest.raises(ValueError, match="Name cannot be longer than 255 characters"):
        Product(name="a" * 256, status=StatusEnum.AVAILABLE)
