from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status, serializers
from .models import Attendance, Class, Cost, Grade, Instructor, Parent, Phone, Phonetype, Room, Student, StudentClass, Subject
from .serializers import AttendanceSerializer, ClassSerializer, CostSerializer, GradeSerializer, InstructorSerializer, ParentSerializer, PhoneSerializer, PhonetypeSerializer, RoomSerializer, StudentClassSerializer, StudentSerializer, SubjectSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class CostViewSet(viewsets.ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhonetypeViewSet(viewsets.ModelViewSet):
    queryset = Phonetype.objects.all()
    serializer_class = PhonetypeSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class StudentClassViewSet(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer




@api_view(['GET'])
def get_student_grades(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    # Optimized Query with Prefetching:
    attendances = Attendance.objects.filter(studentid=student).prefetch_related('classid', 'classid__grade_set')

    classes_and_grades = []

    for attendance in attendances:
        class_instance = attendance.classid
        class_data = ClassSerializer(class_instance).data
        class_data['present'] = attendance.present

        
        grade_obj = next((grade for grade in class_instance.grade_set.all() if grade.studentid == student), None)
        class_data['grade'] = grade_obj.grade if grade_obj else None

        classes_and_grades.append(class_data)

    return Response(classes_and_grades, status=status.HTTP_200_OK)


