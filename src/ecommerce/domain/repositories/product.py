from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID

from ecommerce.domain.entities.product import Product


@dataclass
class ProductRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, product_id: UUID) -> Product | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Product]:
        pass

    @abstractmethod
    def update(self, entity: Product) -> Product:
        pass
