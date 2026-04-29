from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import hello_world, StudentViewSet


router = DefaultRouter()
router.register("students", StudentViewSet, basename="students")


urlpatterns = [
    path("hello/", hello_world, name="hello-world"),
    path("", include(router.urls)),
]