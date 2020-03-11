from rest_framework import serializers
from . models import employees

class employeesSerializers(serializers.ModelSerializer):

    class Meta:
        model = employees
        # fields = ('firstaname', 'lastname')
        fields = '__all__'