import pytest
from rest_framework.test import APIClient

from tests.django_project.mock_data import (
    customer_entity,
    product_entity,
    customer_model,
    product_model,
)


@pytest.mark.django_db
def test_list_products(customer_entity, product_entity, customer_model, product_model):
    client = APIClient()
    response = client.get("/products/")
    assert response.status_code == 200
