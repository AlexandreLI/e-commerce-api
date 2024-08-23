from abc import ABC, abstractmethod
from uuid import UUID

from ecommerce.domain.entities.customer import Customer


class CustomerRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, customer_id: UUID) -> Customer | None:
        pass
