from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage


# Create your views here.


@csrf_exempt
def department_api(request, id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departmentsSerializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departmentsSerializer.data, safe=False)
    elif request.method=='POST':
        departmentData = JSONParser().parse(request)
        departmentSerializer = DepartmentSerializer(data=departmentData)
        if departmentSerializer.is_valid():
            departmentSerializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
        
    elif request.method == 'PUT':
        departmentData = JSONParser().parse(request) 
        department = Departments.objects.get(departmentId=departmentData['departmentId'])
        departmentSerializer = DepartmentSerializer(department, data=departmentData)
        if departmentSerializer.is_valid():
            departmentSerializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        department = Departments.objects.get(departmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully!", safe=False)


@csrf_exempt
def employee_api(request, id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employeesSerializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employeesSerializer.data, safe=False)
    elif request.method=='POST':
        employeeData = JSONParser().parse(request)
        employeeSerializer = EmployeeSerializer(data=employeeData)
        if employeeSerializer.is_valid():
            employeeSerializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
        
    elif request.method == 'PUT':
        employeeData = JSONParser().parse(request) 
        employee = Employees.objects.get(employeeId=employeeData['employeeId'])
        employeeSerializer = EmployeeSerializer(employee, data=employeeData)
        if employeeSerializer.is_valid():
            employeeSerializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        employee = Employees.objects.get(employeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!", safe=False)


@csrf_exempt
def save_file(request):
    file=request.FILES['uploadedFile']
    fileName = default_storage.save(file.name, file)

    return JsonResponse(fileName, safe=False)