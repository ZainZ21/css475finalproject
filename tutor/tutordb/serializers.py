from rest_framework import serializers
from .models import Student, Class, Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['gradenumber']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['starttime', 'roomid', 'instructorid', 'subjectid', 'costid']

class StudentSerializer(serializers.ModelSerializer):
    grade = GradeSerializer(source='gradeid', read_only=True)
    current_classes = ClassSerializer(source='classid', many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'grade', 'current_classes']
