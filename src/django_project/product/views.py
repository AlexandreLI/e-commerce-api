from dataclasses import dataclass

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ecommerce.application.use_cases.product import ListProductUseCase
from django_project.product.repository import DjangoProductRepository
from django_project.reservation.repository import DjangoReservationRepository
from .serializers import ProductResponseSerializer


@dataclass
class ListProductView(APIView):

    use_case: ListProductUseCase = ListProductUseCase(
        product_repo=DjangoProductRepository(),
        reservation_repo=DjangoReservationRepository(),
    )

    def get(self, request: Request) -> Response:
        result = self.use_case.execute()
        data = ProductResponseSerializer(instance=result, many=True).data

        return Response(data, status=status.HTTP_200_OK)
