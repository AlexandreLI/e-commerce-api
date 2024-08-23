from dataclasses import dataclass
from uuid import UUID
from ecommerce.domain.entities.product import StatusEnum


@dataclass
class ProductOutput:
    name: str
    status: StatusEnum
    id: UUID
