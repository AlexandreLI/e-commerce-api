from ecommerce.domain.entities.customer import Customer
from ecommerce.domain.entities.product import Product, StatusEnum
from ecommerce.domain.entities.reservation import Reservation


product_1 = Product(name="Product 1", status=StatusEnum.AVAILABLE)
product_2 = Product(name="Product 2", status=StatusEnum.AVAILABLE)
product_3 = Product(name="Product 3", status=StatusEnum.RESERVED)
product_4 = Product(name="Product 4", status=StatusEnum.UNAVAILABLE)

customer_1 = Customer(name="John Doe")
customer_2 = Customer(name="Alice Doe")

reservation_1 = Reservation(
    customer=customer_1,
    product=product_2,
)

reservation_2 = Reservation(
    customer=customer_2,
    product=product_1,
)

products = [product_1, product_2, product_3, product_4]
customers = [customer_1, customer_2]
reservations = [reservation_1, reservation_2]
