from django.urls import path
from . import views

urlpatterns = [
    path('api/student/<int:student_id>/', views.get_student, name='get_student'),
]
