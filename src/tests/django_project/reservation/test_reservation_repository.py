import pytest

from ecommerce.domain.entities.reservation import Reservation
from django_project.reservation.repository import DjangoReservationRepository
from tests.django_project.mock_data import (
    customer_entity,
    product_entity,
    customer_model,
    product_model,
)


@pytest.mark.django_db
class TestDjangoReservationRepository:
    def test_find_all_by_customer(
        self, customer_entity, product_entity, customer_model, product_model
    ):
        reservation = Reservation(
            product=product_entity,
            customer=customer_entity,
        )
        repository = DjangoReservationRepository()
        repository.create(reservation)
        result = repository.find_all_by_customer(reservation.customer.id)
        assert result[0].id == reservation.id
        assert result[0].customer.id == reservation.customer.id
        assert result[0].product.id == reservation.product.id

    def test_find_all_by_products(
        self, customer_entity, product_entity, customer_model, product_model
    ):
        reservation = Reservation(
            product=product_entity,
            customer=customer_entity,
        )
        repository = DjangoReservationRepository()
        repository.create(reservation)
        result = repository.find_all_by_products([reservation.product.id])
        assert result[0].id == reservation.id
        assert result[0].customer.id == reservation.customer.id
        assert result[0].product.id == reservation.product.id

    def test_create(
        self, customer_entity, product_entity, customer_model, product_model
    ):
        reservation = Reservation(
            product=product_entity,
            customer=customer_entity,
        )
        repository = DjangoReservationRepository()

        result = repository.create(reservation)
        assert result == reservation

    def test_delete(self, customer_entity, product_entity, customer_model, product_model):
        reservation = Reservation(
            product=product_entity,
            customer=customer_entity,
        )
        repository = DjangoReservationRepository()
        repository.create(reservation)
        repository.delete(reservation)
        result = repository.find_all_by_customer(reservation.customer.id)
        assert result == []