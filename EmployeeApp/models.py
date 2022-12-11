from django.db import models

# Create your models here.

class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeesId = models.AutoField(primary_key=True)
    EmployeesName = models.CharField(max_length=500)
    Departament = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)


class vehiculo(model.Models):
    VehiculoId = models.AutoField(primary_key=True)
    VehiculoIdentificador = models.AutoField(primary_key=True)
    VehiculoCaracteritica = models.CharField(max_length=500)
    VehiculoNaional = models.CharField(max_length=500)
    