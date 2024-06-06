from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers, permissions
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Attendance, Class, Cost, Grade, Instructor, Parent, Phone, Phonetype, Room, Student, StudentClass, Subject, Role
from .serializers import AttendanceSerializer, ClassSerializer, CostSerializer, GradeSerializer, InstructorSerializer, ParentSerializer, PhoneSerializer, PhonetypeSerializer, RoomSerializer, StudentClassSerializer, StudentSerializer, SubjectSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class CostViewSet(viewsets.ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [IsAuthenticated]

class PhonetypeViewSet(viewsets.ModelViewSet):
    queryset = Phonetype.objects.all()
    serializer_class = PhonetypeSerializer
    permission_classes = [IsAuthenticated]

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

class StudentClassViewSet(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer
    permission_classes = [IsAuthenticated]



class ClassSerializer(serializers.ModelSerializer):
    instructor = serializers.SerializerMethodField()
    room_number = serializers.IntegerField(source='roomid.roomnumber')   
    building_location = serializers.CharField(source='roomid.buildinglocation')
    subject = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ['id', 'starttime', 'instructor', 'room_number', 'building_location', 'subject', 'cost']  

    def get_instructor(self, obj):
        return f"{obj.instructorid.firstname} {obj.instructorid.lastname}" 

    def get_subject(self, obj):
        return obj.subjectid.name

    def get_cost(self, obj):
        return obj.costid.cost

class StudentGradesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        attendances = (
            Attendance.objects.filter(studentid=student)
            .prefetch_related("classid", "classid__grade_set")
        )

        classes_and_grades = []

        for attendance in attendances:
            class_instance = attendance.classid
            class_data = ClassSerializer(class_instance).data
            class_data["present"] = attendance.present

            grade_obj = class_instance.grade_set.filter(studentid=student).first()  # Filter directly
            class_data["grade"] = grade_obj.grade if grade_obj else None

            classes_and_grades.append(class_data)

        return Response(classes_and_grades, status=status.HTTP_200_OK)


class ClassInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, class_id):
        try:
            class_instance = Class.objects.get(pk=class_id)
        except Class.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)


        serializer = ClassSerializer(class_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)



#unfinished
class CostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, parent_id):
        try:
            parent = Parent.objects.get(pk=parent_id)
        except Parent.DoesNotExist:
            return Response({"error": "Parent not found"}, status=status.HTTP_404_NOT_FOUND)

        # Logic to calculate cost based on parent's children
        students = Student.objects.filter(parent=parent)
    

        
        cost_data = {"parent_id": parent_id, "total_cost": total_cost}  
        serializer = CostSerializer(data=cost_data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


