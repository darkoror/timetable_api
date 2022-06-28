from django.db import connection
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from admin_site.models import Lesson
from retail_site.serializers import LessonSerializer


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
        print(len(connection.queries))
        return Response(data)
