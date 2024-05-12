from django.urls import path
from .views import EmployeeDetail

urlpatterns = [
    path("emp/", EmployeeDetail.as_view(), name = "emp")
]