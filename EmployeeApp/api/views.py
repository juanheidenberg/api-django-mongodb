from rest_framework.viewsets import ModelViewSet
from EmployeeApp.models import Employees
from EmployeeApp.api.serializers import EmployeesSerializer


class EmployeeApiViewSet(ModelViewSet):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()
