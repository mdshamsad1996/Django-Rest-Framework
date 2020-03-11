from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import employees
from . serializers import employeesSerializers
from rest_framework import generics

class DatasetMixin:
    queryset = employees.objects.all()
    lookup_field = 'id'

# Create your views here.

class EmployeeListCreatView(generics.ListCreateAPIView):

    queryset = employees.objects.all()
    serializer_class = employeesSerializers



    
class EmployeeRetriveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = employees.objects.all()
    serializer_class = employeesSerializers

