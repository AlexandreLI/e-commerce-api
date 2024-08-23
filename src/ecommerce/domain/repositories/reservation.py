from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID

from ecommerce.domain.entities.reservation import Reservation


@dataclass
class ReservationRepositoryInterface(ABC):

    @abstractmethod
    def find_all_by_customer(self, customer_id: UUID) -> list[Reservation]:
        pass

    @abstractmethod
    def find_all_by_products(self, products: list[UUID]) -> list[Reservation]:
        pass

    @abstractmethod
    def create(self, entity: Reservation) -> Reservation:
        pass
