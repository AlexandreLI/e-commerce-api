from ecommerce.infra.repositories.in_memory_reservation import (
    InMemoryReservationRepository,
)
from ecommerce.domain.entities.reservation import Reservation
from ecommerce.domain.entities.product import Product, StatusEnum
from tests.ecommerce.mock_data import products, customers, reservations


class TestInMemoryReservationRepository:

    def test_find_all_by_customer(self):

        repository = InMemoryReservationRepository(
            reservations=reservations, customers=customers, products=products
        )
        result = repository.find_all_by_customer(customers[0].id)
        assert result == [reservations[0]]

    def test_find_all_by_products(self):
        repository = InMemoryReservationRepository(
            reservations=reservations, customers=customers, products=products
        )
        result = repository.find_all_by_products(
            products=[product.id for product in products]
        )
        assert result == reservations

    def test_create(self):
        product_list = [Product(name="Product 1", status=StatusEnum.AVAILABLE)]
        reservation = Reservation(
            customer=customers[0],
            product=product_list[0],
        )
        repository = InMemoryReservationRepository(
            [], products=product_list, customers=customers
        )
        repository.create(reservation)
        result = repository.find_all_by_customer(customers[0].id)
        assert result == [reservation]
