from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, ClassViewSet, CostViewSet, GradeViewSet, InstructorViewSet, ParentViewSet, PhoneViewSet, PhonetypeViewSet, RoomViewSet, StudentViewSet, SubjectViewSet

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

urlpatterns = [
    path('', include(router.urls)),
]
