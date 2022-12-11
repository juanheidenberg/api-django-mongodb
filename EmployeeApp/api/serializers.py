from rest_framework.serializers import ModelSerializer
from EmployeeApp.models import Employees


class EmployeesSerializer(ModelSerializer):
    class Meta:
      model = Employees
      fields = ['EmployeesId','EmployeesName','Departament','DateOfJoining','PhotoFileName' ]
