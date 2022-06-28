from rest_framework import serializers

from admin_site.models import Lesson, Teacher, Subject


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'lesson_number', 'type', 'subgroup', 'week_day', 'lesson_url', 'frequency',
            'additional_info', 'teachers', 'subject_id', 'academy_building_id', 'auditorium_id'
        )


class TeacherShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'short_name')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')
