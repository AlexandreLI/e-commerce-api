from dataclasses import dataclass
from uuid import UUID

from datetime import datetime


@dataclass
class ProductReservetionOutput:
    id: UUID
    name: str
    status: str


@dataclass
class CustomerReservetionOutput:
    id: UUID
    name: str


@dataclass
class CustomerProductReservetionOutput:
    id: UUID
    product: ProductReservetionOutput
    customer: CustomerReservetionOutput
    reserved_at: datetime
