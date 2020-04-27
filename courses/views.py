from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EvaluationsAPIView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()

class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(), 
                                    course_id=self.kwargs.get('course_pk'), 
                                    pk=self.kwargs.get('evaluation_pk'))
        return get_object_or_404(self.get_queryset(),
                                pk=self.kwargs.get('evaluation_pk'))
    