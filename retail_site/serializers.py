from rest_framework import serializers

from admin_site.models import Lesson, Teacher, Subject, University, Department, Group


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'name')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class LessonSerializer(serializers.ModelSerializer):
    auditorium = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = (
            'lesson_number', 'type', 'subgroup', 'week_day', 'lesson_url', 'frequency',
            'additional_info', 'teachers', 'subject_id', 'academy_building', 'auditorium'
        )

    def get_auditorium(self, lesson) -> str:
        return lesson.auditorium.name


class TeacherShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'short_name')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')
