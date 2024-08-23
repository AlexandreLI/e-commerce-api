from dataclasses import dataclass
from uuid import UUID

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ecommerce.application.use_cases.customer import (
    ListCustomerProductsReservationUseCase,
)
from ecommerce.application.use_cases.exceptions import ReservationNotFoundException
from django_project.reservation.repository import DjangoReservationRepository
from django_project.product.repository import DjangoProductRepository
from .serializers import CustomerReservationResponseSerializer


@dataclass
class ListCustomerReservedProductsView(APIView):
    use_case: ListCustomerProductsReservationUseCase = (
        ListCustomerProductsReservationUseCase(
            reservation_repository=DjangoReservationRepository(),
            product_repository=DjangoProductRepository(),
        )
    )

    def get(self, request: Request, customer_id: UUID) -> Response:
        try:
            output = self.use_case.execute(customer_id=customer_id)
        except ReservationNotFoundException as error:
            return Response({"message": str(error)}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerReservationResponseSerializer(
            instance=output, many=True
        ).data
        return Response(serializer, status=status.HTTP_200_OK)
