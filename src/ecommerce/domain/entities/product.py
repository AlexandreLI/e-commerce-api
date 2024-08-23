from dataclasses import dataclass, field
from uuid import UUID, uuid4
from enum import Enum


class StatusEnum(Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    RESERVED = "reserved"


@dataclass
class Product:
    name: str
    status: StatusEnum
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        self.validate_status()
        self.validate_name()

    def validate_name(self):
        if not self.name:
            raise ValueError("Name cannot be empty")

        if len(self.name) > 255:
            raise ValueError("Name cannot be longer than 255 characters")

    def validate_status(self):
        if not isinstance(self.status, StatusEnum):
            raise ValueError(
                f"Invalid status '{self.status}'. Must be one of: {[status.value for status in StatusEnum]}"
            )

        if not self.name:
            raise ValueError("Name cannot be empty")

    def update_status(self, status: StatusEnum):
        self.status = status
