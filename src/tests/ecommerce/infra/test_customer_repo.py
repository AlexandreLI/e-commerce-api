from ecommerce.infra.repositories.in_memory_customer import InMemoryCustomerRepository
from tests.ecommerce.mock_data import customers


class TestInMemoryCustomerRepository:

    def test_get_by_id(self):
        repository = InMemoryCustomerRepository(customers=customers)
        result = repository.get_by_id(customers[0].id)
        assert result == customers[0]
