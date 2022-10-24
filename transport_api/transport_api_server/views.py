from .models import Clients, Orders, Trips, Licenses, Cars, Drivers
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import (
    ClientsSerializer,
    OrdersSerializer,
    TripsSerializer,
    CarsSerializer,
    LicensesSerializer,
    DriversSerializer,
)


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class LicensesViewSet(viewsets.ModelViewSet):
    queryset = Licenses.objects.all()
    serializer_class = LicensesSerializer


class DriversViewSet(viewsets.ModelViewSet):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer


def custom404(request, exception=None):
    return JsonResponse({"detail": "Not found."})
