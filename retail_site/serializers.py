from rest_framework import serializers

from admin_site.models import Lesson


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'lesson_number', 'type', 'subgroup', 'week_day', 'lesson_url', 'frequency',
            'additional_info', 'teachers', 'groups', 'subject', 'auditorium'
        )
