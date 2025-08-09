from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
class Employee(models.model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

class Project(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee, related_name='projects')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='projects')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects')