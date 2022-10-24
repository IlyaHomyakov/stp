from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db.models import Q, F
from django.db import models


class Clients(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    phone = models.CharField(max_length=11, unique=True)

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"
        ordering = ("full_name",)

    def __str__(self):
        return self.full_name


class Orders(models.Model):
    client = models.ForeignKey("Clients", on_delete=models.PROTECT, null=True)
    volume = models.FloatField(verbose_name="Order volume, m^3")
    weight = models.IntegerField(verbose_name="Order weight, kg")
    ship_date = models.DateField()  # when trip started
    recovery_date = models.DateField()  # when trip ended
    shipment_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Shipment price, BYN"
    )

    class Meta:
        verbose_name = "Orders"
        verbose_name_plural = "Orders"
        ordering = ("ship_date",)
        constraints = [
            models.CheckConstraint(
                check=Q(recovery_date__gt=F("ship_date")),
                name="ship_recovery_date_constraint",
            )
        ]

    def __str__(self):
        return f"Order for {self.client} ({self.weight}kg, {self.volume}m^3)"


class Trips(models.Model):
    order = models.ForeignKey("Orders", on_delete=models.PROTECT)
    car = models.ForeignKey("Cars", on_delete=models.PROTECT)
    driver = models.ForeignKey("Drivers", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Trips"
        verbose_name_plural = "Trips"

    def __str__(self):
        return f"Trip for {self.driver}"

    def clean(self):
        order_volume = self.order.volume
        car_volume = self.car.volume
        order_weight = self.order.weight
        car_max_payload = self.car.payload
        car_license = self.car.license.category
        drive_license = self.driver.license.category

        if order_volume > car_volume:
            raise ValidationError(
                _(
                    f"Order volume ({order_volume}m^3) can not be greater than car trunk volume ({car_volume}m^3). "
                    f"Choose another car."
                )
            )
        if order_weight > car_max_payload:
            raise ValidationError(
                _(
                    f"Order weight ({order_weight}kg) can not be greater than car max payload ({car_max_payload}kg). "
                    f"Choose another car."
                )
            )
        if drive_license != car_license:
            raise ValidationError(
                _(
                    f"Driver {self.driver.full_name} is not allowed to drive selected car. Choose another driver."
                )
            )


class Cars(models.Model):
    vin = models.CharField(max_length=17)
    model = models.CharField(max_length=255)
    license = models.ForeignKey(
        "Licenses",
        on_delete=models.PROTECT,
        verbose_name="Required license",
    )
    volume = models.FloatField(verbose_name="Car trunk volume, m^3")
    payload = models.IntegerField(verbose_name="Car maximum load, kg")

    class Meta:
        verbose_name = "Cars"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.model} cat. {self.license.category} ({self.payload}kg, {self.volume}m^3)"


class Licenses(models.Model):
    category = models.CharField(max_length=2, unique=True)

    class Meta:
        verbose_name = "Licenses"
        verbose_name_plural = "Licenses"
        ordering = ("category",)

    def __str__(self):
        return self.category


class Drivers(models.Model):
    full_name = models.CharField(max_length=255, default="Driver Name By Default")
    license = models.ForeignKey("Licenses", on_delete=models.PROTECT)
    birth_date = models.DateField()

    class Meta:
        verbose_name = "Drivers"
        verbose_name_plural = "Drivers"
        ordering = ("full_name",)

    def __str__(self):
        return f"{self.full_name} cat. {self.license}"
