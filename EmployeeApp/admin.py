from django.contrib import admin
from EmployeeApp.models import Employees


@admin.register(Employees)
class EmployeeAppAdmin(admin.ModelAdmin):
    list_display = ['EmployeesId','EmployeesName','Departament','DateOfJoining','PhotoFileName']
