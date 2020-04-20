from django.urls import path

from .views import CourseAPIView, EvaluationAPIView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('evaluations/', EvaluationAPIView.as_view(), name='evaluations')
]