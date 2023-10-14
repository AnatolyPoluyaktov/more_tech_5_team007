from rest_framework.routers import DefaultRouter
from src.core.views import (
    AtmViewSet,
    AtmServiceViewSet,
    OfficeViewSet,
    SchedulerViewset,
)

platform_router = DefaultRouter()

platform_router.register("offices", OfficeViewSet, "OfficeViewSet")
platform_router.register("atm-services", AtmServiceViewSet, "AtmServiceViewset")
platform_router.register('atms', AtmViewSet, "AtmViewSet")
platform_router.register("schedulers", SchedulerViewset, "SchedulerViewset")

urlpatterns = platform_router.urls
