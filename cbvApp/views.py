from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class StudentPagination(PageNumberPagination):
    page_size = 2

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination