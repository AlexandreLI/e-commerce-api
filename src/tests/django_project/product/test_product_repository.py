import pytest
from django_project.product.repository import DjangoProductRepository
from tests.django_project.mock_data import product_entity, product_model


@pytest.mark.django_db
class TestDjangoProductRepository:
    def test_get_by_id(self, product_entity, product_model):
        repository = DjangoProductRepository()
        result = repository.get_by_id(product_entity.id)
        assert result == product_entity

    def test_get_all(self, product_entity, product_model):
        repository = DjangoProductRepository()
        result = repository.get_all()
        assert result == [product_entity]

    def test_update(self, product_entity, product_model):
        repository = DjangoProductRepository()
        result = repository.update(product_entity)
        assert result == product_entity