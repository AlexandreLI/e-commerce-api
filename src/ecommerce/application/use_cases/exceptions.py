from uuid import UUID


class NotFoundException(Exception):
    def __init__(self, id: UUID, entity: str):
        super().__init__(f"{entity} with id {id} not found")


class ReservationNotFoundException(Exception):
    def __init__(self, customer_id: UUID):
        super().__init__(f"Reservation with customer id {customer_id} not found")


class InvalidReservationException(Exception):
    pass
