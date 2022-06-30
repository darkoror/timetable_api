from django.db import connection
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from admin_site.models import Lesson, Teacher, Subject
from retail_site.serializers import LessonSerializer, TeacherShortSerializer, SubjectSerializer


class GroupLessonsAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = LessonSerializer

    def get_queryset(self):
        return (
            Lesson.objects.filter(groups=self.kwargs.get('group_id'))
            .select_related('auditorium')
            .prefetch_related('teachers')
            .order_by('week_day', 'lesson_number')
        )

    def list(self, request, *args, **kwargs):
        data = self.serializer_class(self.get_queryset(), many=True).data
        return Response(data)


class GroupTeachersAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = TeacherShortSerializer

    def get_queryset(self):
        return Teacher.objects.filter(lessons__groups=self.kwargs.get('group_id')).distinct()


class GroupSubjectsAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.filter(lessons__groups=self.kwargs.get('group_id')).distinct()
