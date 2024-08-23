from uuid import UUID
from ecommerce.domain.repositories.product import ProductRepositoryInterface
from ecommerce.domain.entities.product import Product, StatusEnum
from .models import Product as ProductModel


class DjangoProductRepository(ProductRepositoryInterface):
    def get_by_id(self, product_id: UUID) -> Product | None:
        product = ProductModel.objects.filter(id=product_id).first()
        if not product:
            return None
        return Product(
            id=product.id,
            name=product.name,
            status=StatusEnum[product.status.upper()],
        )

    def get_all(self) -> list[Product]:
        products = ProductModel.objects.all()
        return [
            Product(
                id=product.id,
                name=product.name,
                status=StatusEnum[product.status.upper()],
            )
            for product in products
        ]

    def update(self, entity: Product) -> Product:
        product = ProductModel.objects.filter(id=entity.id).first()
        product.status = entity.status.value
        product.save()
        return Product(
            id=product.id,
            name=product.name,
            status=StatusEnum[product.status.upper()],
        )
