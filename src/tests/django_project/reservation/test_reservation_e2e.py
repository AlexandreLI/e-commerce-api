import pytest
from rest_framework.test import APIClient

from tests.django_project.mock_data import (
    customer_entity,
    product_entity,
    customer_model,
    product_model,
    product_model_unavailable,
    product_entity_unavailable,
    product_entity_reserved,
    product_model_reserved,
)


@pytest.mark.django_db
def test_create_reservation(
    customer_entity, product_entity, customer_model, product_model
):
    client = APIClient()
    response = client.post(
        f"/products/{product_entity.id}/reserve",
        {"customer_id": f"{customer_entity.id}"},
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_reservation_customer_not_found(
    customer_entity, product_entity, customer_model, product_model
):
    client = APIClient()
    response = client.post(
        f"/products/{product_entity.id}/reserve",
        {"customer_id": "00000000-0000-0000-0000-000000000000"},
    )
    assert response.status_code == 404
    assert (
        response.data["message"]
        == "Customer with id 00000000-0000-0000-0000-000000000000 not found"
    )


@pytest.mark.django_db
def test_create_reservation_product_not_found(
    customer_entity, product_entity, customer_model, product_model
):
    client = APIClient()
    response = client.post(
        f"/products/00000000-0000-0000-0000-000000000000/reserve",
        {"customer_id": f"{customer_entity.id}"},
    )
    assert response.status_code == 404
    assert (
        response.data["message"]
        == "Product with id 00000000-0000-0000-0000-000000000000 not found"
    )


@pytest.mark.django_db
def test_create_reservation_product_not_available(
    customer_entity,
    product_entity_unavailable,
    customer_model,
    product_model_unavailable,
):
    client = APIClient()
    response = client.post(
        f"/products/{product_entity_unavailable.id}/reserve",
        {"customer_id": f"{customer_entity.id}"},
    )
    assert response.status_code == 400
    assert response.data["message"] == "Product unavailable or already reserved"


@pytest.mark.django_db
def test_create_reservation_product_reserved(
    customer_entity,
    product_entity_reserved,
    customer_model,
    product_model_reserved,
):
    client = APIClient()
    response = client.post(
        f"/products/{product_entity_reserved.id}/reserve",
        {"customer_id": f"{customer_entity.id}"},
    )
    assert response.status_code == 400
    assert response.data["message"] == "Product unavailable or already reserved"
