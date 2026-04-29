from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer


@api_view(["GET"])
def hello_world(request):
    return Response({
        "message": "Hello World from Django REST API!"
    })


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("-created_at")
    serializer_class = StudentSerializer