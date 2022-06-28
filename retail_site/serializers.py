from rest_framework import serializers

from admin_site.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'lesson_number', 'type', 'subgroup', 'week_day', 'lesson_url', 'frequency',
            'additional_info', 'teachers', 'subject_id', 'academy_building_id', 'auditorium_id'
        )
