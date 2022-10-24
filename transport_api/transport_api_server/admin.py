from .models import Clients, Orders, Trips, Licenses, Cars, Drivers
from django.contrib.auth.models import User, Group
from django.contrib import admin

admin.site.site_header = "Transport Company Observer"

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "birth_date",
        "phone",
    )


@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "car",
        "driver",
    )


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = (
        "vin",
        "model",
        "license",
        "volume",
        "payload",
    )


@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "license",
        "birth_date",
    )
    list_filter = ("license",)


@admin.register(Licenses)
class LicensesAdmin(admin.ModelAdmin):
    list_display = ("category",)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "volume",
        "weight",
        "ship_date",
        "recovery_date",
        "shipment_price",
    )
