from django.urls import path

from .views import CourseAPIView, EvaluationAPIView, CoursesAPIView, EvaluationsAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('courses/<int:course_pk>/evaluations', EvaluationsAPIView.as_view(), name='course_evaluations'),
    path('courses/<int:course_pk>/evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='course_evaluation'),

    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:evaluation_pk>/', EvaluationAPIView.as_view(), name='evaluation')
]