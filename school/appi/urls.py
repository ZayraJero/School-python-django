from rest_framework import routers
from django.urls import path, include
from .views import BootcampViewSet, KoderViewSet

router = routers.DefaultRouter()
router.register("bootcamps", BootcampViewSet)
router.register("koders", KoderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]