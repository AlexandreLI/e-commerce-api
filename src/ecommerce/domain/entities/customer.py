from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Customer:
    name: str
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        self.validate_name()

    def validate_name(self):
        if not self.name:
            raise ValueError("Name cannot be empty")

        if len(self.name) > 255:
            raise ValueError("Name cannot be longer than 255 characters")
