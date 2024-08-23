from uuid import UUID

from ecommerce.domain.entities.customer import Customer
from ecommerce.domain.entities.product import Product, StatusEnum
from ecommerce.domain.entities.reservation import Reservation
from ecommerce.domain.repositories.reservation import ReservationRepositoryInterface
from django_project.reservation.models import Reservation as ReservationModel


class DjangoReservationRepository(ReservationRepositoryInterface):
    def find_all_by_customer(self, customer_id: UUID) -> list[Reservation]:
        result = ReservationModel.objects.filter(customer_id=customer_id)
        return [
            Reservation(
                product=Product(
                    id=reservation.product.id,
                    name=reservation.product.name,
                    status=StatusEnum[reservation.product.status.upper()],
                ),
                customer=Customer(
                    id=reservation.customer.id, name=reservation.customer.name
                ),
                reserved_at=reservation.reservation_date,
                id=reservation.id,
            )
            for reservation in result
        ]

    def find_all_by_products(self, products: list[UUID]) -> list[Reservation]:
        result = ReservationModel.objects.filter(product_id__in=products)
        return [
            Reservation(
                product=Product(
                    id=reservation.product.id,
                    name=reservation.product.name,
                    status=StatusEnum(reservation.product.status),
                ),
                customer=Customer(
                    id=reservation.customer.id, name=reservation.customer.name
                ),
                reserved_at=reservation.reservation_date,
                id=reservation.id,
            )
            for reservation in result
        ]

    def create(self, entity: Reservation) -> Reservation:

        reservation_model = ReservationModel.objects.create(
            customer_id=entity.customer.id,
            product_id=entity.product.id,
            reservation_date=entity.reserved_at,
            id=entity.id,
        )
        reservation_model.save()
        return Reservation(
            product=Product(
                id=reservation_model.product.id,
                name=reservation_model.product.name,
                status=StatusEnum(reservation_model.product.status),
            ),
            customer=Customer(
                id=reservation_model.customer.id,
                name=reservation_model.customer.name,
            ),
            reserved_at=reservation_model.reservation_date,
            id=reservation_model.id,
        )
