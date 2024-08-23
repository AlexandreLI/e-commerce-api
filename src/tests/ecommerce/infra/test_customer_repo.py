from uuid import UUID
from ecommerce.infra.repositories.in_memory_customer import InMemoryCustomerRepository
from tests.ecommerce.mock_data import customers


class TestInMemoryCustomerRepository:

    def test_get_by_id(self):
        repository = InMemoryCustomerRepository(customers=customers)
        result = repository.get_by_id(customers[0].id)
        assert result == customers[0]

    def test_not_found(self):
        repository = InMemoryCustomerRepository(customers=customers)
        result = repository.get_by_id(UUID("00000000-0000-0000-0000-000000000000"))
        assert result is None
