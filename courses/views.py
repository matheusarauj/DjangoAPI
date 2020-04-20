from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

class CourseAPIView(APIView):
    """
    API Courses
    """
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class EvaluationAPIView(APIView):
    """
    API Evaluation
    """
    def get(self, request):
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

        