from dataclasses import dataclass
from uuid import UUID
import datetime


@dataclass
class ReservationOutput:
    product_id: UUID
    customer_id: UUID
    reserved_at: datetime.datetime
    id: UUID
