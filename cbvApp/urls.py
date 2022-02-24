from django.urls import path
from cbvApp.views import StudentList,StudentDetail

urlpatterns = [
    path('students', StudentList.as_view()),
    path('student/<int:pk>',StudentDetail.as_view()),
]