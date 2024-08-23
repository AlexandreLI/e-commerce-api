from uuid import UUID

from ecommerce.domain.repositories.customer import CustomerRepositoryInterface
from ecommerce.domain.entities.customer import Customer
from .models import Customer as CustomerModel


class DjangoCustomerRepository(CustomerRepositoryInterface):
    def get_by_id(self, customer_id: UUID) -> Customer | None:
        customer = CustomerModel.objects.filter(id=customer_id).first()
        if not customer:
            return None
        return Customer(id=customer.id, name=customer.name)
