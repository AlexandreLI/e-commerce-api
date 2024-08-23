from uuid import UUID

from ecommerce.domain.repositories.customer import (
    CustomerRepositoryInterface as Interface,
)
from ecommerce.domain.entities.customer import Customer


class InMemoryCustomerRepository(Interface):
    def __init__(self, customers: list[Customer] = []):
        self.customers = customers

    def get_by_id(self, customer_id: UUID) -> Customer | None:
        return next(
            (customer for customer in self.customers if customer.id == customer_id),
            None,
        )
