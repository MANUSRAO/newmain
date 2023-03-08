from rest_framework import serializers
from .models import Student, Holiday
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class holidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'