from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from admin_site.models import Lesson, Teacher, Subject, University, Department, Group
from retail_site.serializers import LessonSerializer, TeacherShortSerializer, SubjectSerializer, UniversitySerializer, \
    DepartmentSerializer, GroupSerializer


class UniversityAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class DepartmentAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        university = get_object_or_404(University, id=self.kwargs.get('university_id'))
        return Department.objects.filter(university=university)


class GroupAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = GroupSerializer

    def get_queryset(self):
        department = get_object_or_404(Department, id=self.kwargs.get('department_id'))
        return Group.objects.filter(department=department)


class LessonsAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = LessonSerializer

    def get_queryset(self):
        group = get_object_or_404(Group, id=self.kwargs.get('group_id'))
        return (
            Lesson.objects.filter(groups=group)
            .select_related('auditorium__academy_building')
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
        group = get_object_or_404(Group, id=self.kwargs.get('group_id'))
        return Teacher.objects.filter(lessons__groups=group).distinct()


class GroupSubjectsAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = SubjectSerializer

    def get_queryset(self):
        group = get_object_or_404(Group, id=self.kwargs.get('group_id'))
        return Subject.objects.filter(lessons__groups=group).distinct()
