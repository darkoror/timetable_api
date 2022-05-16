from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from admin_site.models import Lesson
from retail_site.serializers import ScheduleSerializer


class ScheduleAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return (
            Lesson.objects.filter(groups=self.kwargs.get('group_id'))
            .select_related('subject', 'auditorium__academy_building', 'auditorium')
            .prefetch_related('teachers')
        )

    def retrieve(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset(), many=True).data)
