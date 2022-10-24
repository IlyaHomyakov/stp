from .models import Clients, Orders, Trips, Licenses, Cars, Drivers
from rest_framework import serializers


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = "__all__"


class LicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenses
        fields = "__all__"


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"


class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = "__all__"
