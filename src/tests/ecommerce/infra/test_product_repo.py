from ecommerce.infra.repositories.in_memory_product import (
    InMemoryProductRepository,
)
from ecommerce.domain.entities.product import Product, StatusEnum
from tests.ecommerce.mock_data import products


class TestProductInMemoryRepository:

    def test_get_all(self):
        repository = InMemoryProductRepository(products=products)
        result = repository.get_all()
        assert result == products

    def test_get_by_id(self):
        repository = InMemoryProductRepository(products=products)
        result = repository.get_by_id(products[0].id)
        assert result == products[0]

    def test_update(self):
        repository = InMemoryProductRepository(products=products)
        product = Product(
            id=products[0].id,
            name="Product 1",
            status=StatusEnum.AVAILABLE,
        )
        repository.update(product)
        result = repository.get_by_id(products[0].id)
        assert result == product
