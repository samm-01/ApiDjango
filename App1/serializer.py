from pyexpat import model
from rest_framework import serialzers
from .models import employee

class EmployeeSerializer(serialzers.ModelSerialzer):
    class Meta:
        model = employee
        fields = "__all__"