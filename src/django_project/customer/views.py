from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .repository import DjangoCustomerRepository


class ListCustomerReservedProductsView(APIView):

    def get(self, request: Request) -> Response:
        pass
