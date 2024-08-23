import pytest
from rest_framework.test import APIClient

from tests.django_project.mock_data import (
    customer_entity,
    product_entity,
    reservation_entity,
    customer_model,
    product_model,
    reservation_model,
)


@pytest.mark.django_db
def test_get_list_of_customer_reservations(
    customer_entity,
    product_entity,
    customer_model,
    product_model,
    reservation_model,
    reservation_entity,
):
    client = APIClient()
    response = client.get(f"/customer/{customer_entity.id}/reservations")
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_list_of_customer_reservations_not_found(
    customer_entity,
    product_entity,
    customer_model,
    product_model,
    reservation_model,
    reservation_entity,
):
    client = APIClient()
    response = client.get(
        f"/customer/00000000-0000-0000-0000-000000000000/reservations"
    )
    assert response.status_code == 404
    assert (
        response.data["message"]
        == "Reservation with customer id 00000000-0000-0000-0000-000000000000 not found"
    )
