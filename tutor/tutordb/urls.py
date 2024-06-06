from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, ClassViewSet, CostViewSet, GradeViewSet, InstructorViewSet, ParentViewSet, PhoneViewSet, PhonetypeViewSet, RoomViewSet, StudentClassViewSet, StudentViewSet, SubjectViewSet, StudentGradesView, ClassInfoView, CostView

router = DefaultRouter()
router.register(r'attendance', AttendanceViewSet)
router.register(r'class', ClassViewSet)
router.register(r'cost', CostViewSet)
router.register(r'grade', GradeViewSet)
router.register(r'instructor', InstructorViewSet)
router.register(r'parent', ParentViewSet)
router.register(r'phone', PhoneViewSet)
router.register(r'phonetype', PhonetypeViewSet)
router.register(r'room', RoomViewSet)
router.register(r'student', StudentViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'studentclass', StudentClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('student-grades/<int:student_id>/', StudentGradesView.as_view(), name='get_student_grades'),
    path('class-info/<int:class_id>/', ClassInfoView.as_view(), name='get_class_information'),
    path('get_cost/<int:parent_id>/', CostView.as_view(), name='get_cost'),
    
]
