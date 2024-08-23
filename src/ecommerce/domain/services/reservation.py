from ecommerce.domain.entities.reservation import Reservation
from ecommerce.domain.entities.product import Product, StatusEnum


class ReservationService:
    @staticmethod
    def check_reservation_expiration(
        reservations: list[Reservation], products: list[Product]
    ) -> list[Product]:
        return [
            product
            for product in products
            if any(
                reservation.product.id == product.id and reservation.is_expired()
                for reservation in reservations
            )
        ]
