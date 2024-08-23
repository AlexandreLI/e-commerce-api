from ecommerce.domain.repositories.product import (
    ProductRepositoryInterface as Interface,
)
from ecommerce.domain.entities.product import Product
from uuid import UUID


class InMemoryProductRepository(Interface):
    def __init__(self, products: list[Product] = []):
        self.products = products

    def get_by_id(self, product_id: UUID) -> Product | None:
        return next(
            (product for product in self.products if product.id == product_id), None
        )

    def get_all(self) -> list[Product]:
        return self.products

    def update(self, entity: Product) -> Product:
        product = next(
            (product for product in self.products if product.id == entity.id), None
        )

        product.status = entity.status
        return product
