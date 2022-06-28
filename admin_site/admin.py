from django.contrib import admin

from admin_site.models import University, Department, Group, Teacher, Subject, Lesson, Auditorium, AcademyBuilding


@admin.register(University)
class AdminUniversity(admin.ModelAdmin):
    list_display = ('name', 'week_type')


@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    list_display = ('name', 'university')


@admin.register(Group)
class AdminDepartment(admin.ModelAdmin):
    list_display = ('name', 'department')


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic')
    fields = ('surname', 'name', 'patronymic', 'universities')


@admin.register(Subject)
class AdminSubject(admin.ModelAdmin):
    list_display = ('name', 'university')


@admin.register(AcademyBuilding)
class AdminAcademyBuilding(admin.ModelAdmin):
    list_display = ('name', 'university')


@admin.register(Auditorium)
class AdminAuditorium(admin.ModelAdmin):
    list_display = ('name', 'academy_building')


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = (
        'lesson_number', 'type', 'subgroup', 'week_day', 'lesson_url', 'frequency',
        'additional_info', 'subject', 'auditorium', 'created_date', 'updated_date'
    )
    fields = (
        'groups', 'week_day', 'lesson_number', 'subgroup', 'frequency', 'subject', 'teachers', 'type', 'auditorium',
        'lesson_url', 'additional_info',
    )
