from ecommerce.domain.repositories.reservation import (
    ReservationRepositoryInterface as Interface,
)
from ecommerce.domain.entities.reservation import Reservation
from ecommerce.domain.entities.product import Product
from ecommerce.domain.entities.customer import Customer
from uuid import UUID


class InMemoryReservationRepository(Interface):
    def __init__(
        self,
        reservations: list[Reservation] = [],
        customers: list[Customer] = [],
        products: list[Product] = [],
    ):
        self.reservations = reservations
        self.products = products
        self.customers = customers

    def find_all_by_customer(self, customer_id: UUID) -> list[Reservation]:
        return [
            reservation
            for reservation in self.reservations
            if reservation.customer.id == customer_id
        ]

    def find_all_by_products(self, products: list[UUID]) -> list[Reservation]:
        return [
            reservation
            for reservation in self.reservations
            if reservation.product.id in products
        ]

    def create(self, entity: Reservation) -> Reservation:
        self.reservations.append(entity)
        return entity

    def delete(self, entity: Reservation) -> None:
        self.reservations.remove(entity)
