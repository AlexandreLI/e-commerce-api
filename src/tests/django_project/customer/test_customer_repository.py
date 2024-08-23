import pytest
from uuid import UUID

from django_project.customer.repository import DjangoCustomerRepository
from tests.django_project.mock_data import customer_entity, customer_model


@pytest.mark.django_db
class TestDjangoCustomerRepository:

    def test_get_by_id(self, customer_entity, customer_model):
        repository = DjangoCustomerRepository()
        result = repository.get_by_id(customer_entity.id)
        assert result.id == customer_entity.id
        assert result.name == customer_entity.name

    def test_not_found(self, customer_entity, customer_model):
        repository = DjangoCustomerRepository()
        result = repository.get_by_id(UUID("00000000-0000-0000-0000-000000000000"))
        assert result is None
