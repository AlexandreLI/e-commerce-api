from uuid import UUID
from dataclasses import dataclass

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from ecommerce.application.use_cases.product import ListProductUseCase


@dataclass
class ListProductView(APIView):

    use_case: ListProductUseCase = None

    def get(self, request: Request) -> Response:
        pass
