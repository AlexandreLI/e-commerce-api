from uuid import UUID
from dataclasses import dataclass

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ecommerce.application.use_cases.reservation import (
    CreateReservationUseCase,
)
from src.ecommerce.application.use_cases.exceptions import (
    InvalidReservationException,
    NotFoundException,
)
from .serializers import ReservationResponseSerializer, ReservationRequestSerializer
from .repository import DjangoReservationRepository
from django_project.product.repository import DjangoProductRepository
from django_project.customer.repository import DjangoCustomerRepository


@dataclass
class ReserveProductView(APIView):

    use_case: CreateReservationUseCase = CreateReservationUseCase(
        reservation_repo=DjangoReservationRepository(),
        product_repo=DjangoProductRepository(),
        customer_repo=DjangoCustomerRepository(),
    )

    def post(self, request: Request, product_id: UUID) -> Response:
        serializer = ReservationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        input_params = CreateReservationUseCase.InputParams(
            product_id=product_id, customer_id=serializer.data.get("customer_id")
        )
        try:
            result = self.use_case.execute(input_params=input_params)
        except NotFoundException as error:
            return Response({"message": str(error)}, status=status.HTTP_404_NOT_FOUND)
        except (InvalidReservationException, ValueError) as error:
            return Response({"message": str(error)}, status=status.HTTP_400_BAD_REQUEST)

        output_serializer = ReservationResponseSerializer(instance=result)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
