from dataclasses import dataclass

from ecommerce.domain.repositories.product import ProductRepositoryInterface
from ecommerce.domain.repositories.reservation import ReservationRepositoryInterface
from ecommerce.domain.entities.product import StatusEnum
from ecommerce.application.dto.product import ProductOutput
from ecommerce.domain.services.reservation import ReservationService


@dataclass(frozen=True)
class ListProductUseCase:
    product_repo: ProductRepositoryInterface
    reservation_repo: ReservationRepositoryInterface
    reservation_service = ReservationService()

    def execute(self) -> list[ProductOutput]:
        products = self.product_repo.get_all()

        reservations = self.reservation_repo.find_all_by_products(
            [product.id for product in products]
        )
        products_to_update = self.reservation_service.check_reservation_expiration(
            reservations, products
        )

        for product in products_to_update:
            self.product_repo.update(product)

        if products_to_update:
            products = self.product_repo.get_all()

        return [
            ProductOutput(name=product.name, status=product.status.value, id=product.id)
            for product in products
        ]
