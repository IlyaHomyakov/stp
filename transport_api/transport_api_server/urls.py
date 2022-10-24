from django.urls import path, include
from rest_framework import routers
from .views import (
    LicensesViewSet,
    ClientsViewSet,
    DriversViewSet,
    OrdersViewSet,
    TripsViewSet,
    CarsViewSet,
)

router = routers.DefaultRouter()
router.register(r"licenses", LicensesViewSet)
router.register(r"clients", ClientsViewSet)
router.register(r"drivers", DriversViewSet)
router.register(r"orders", OrdersViewSet)
router.register(r"trips", TripsViewSet)
router.register(r"cars", CarsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
