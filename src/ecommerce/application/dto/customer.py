from dataclasses import dataclass
from uuid import UUID


@dataclass
class CustomerProductReservetionOutput:
    product_id: UUID
    product_name: str
