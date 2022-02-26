from django.urls import path, include
from cbvApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students',views.StudentViewSet)

urlpatterns = [
   path('',include(router.urls)),
]