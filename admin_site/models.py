from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Frequency:
    """
    There are lessons which occur not regular (only once in 2 weeks)
    So the first week we call NUMERATOR (чисельник), and the other DENOMINATOR (знаменник)
    """

    WEEKLY = 0  # Щотижня
    NUMERATOR = 1  # Чисельник
    DENOMINATOR = 2  # Знаменник

    # Used in University model (indicates, type of the week, and according to that what lessons should occur)
    WEEK_FREQUENCY_TYPES = (
        (NUMERATOR, 'Numerator'),
        (DENOMINATOR, 'Denominator'),
    )

    # Used in Lesson model (indicates when lesson occurs)
    LESSON_FREQUENCY = (
        (WEEKLY, 'Every week'),
        (NUMERATOR, 'Numerator'),
        (DENOMINATOR, 'Denominator'),
    )


class University(models.Model):
    name = models.CharField(max_length=200, unique=True)
    week_type = models.PositiveSmallIntegerField(
        choices=Frequency.WEEK_FREQUENCY_TYPES,
        help_text='indicates what lessons should occur (there are lessons occur once in 2 weeks)'
    )

    class Meta:
        db_table = 'universities'
        verbose_name = 'university'
        verbose_name_plural = 'universities'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, related_name='departments', on_delete=models.CASCADE)

    class Meta:
        db_table = 'departments'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'university'],
                name='unique_university_department',
            )
        ]

    def __str__(self):
        return f'{self.name} - {self.university}'


class Group(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name='groups', on_delete=models.CASCADE)

    class Meta:
        db_table = 'groups'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'department'],
                name='unique_group_in_department',
            )
        ]

    def __str__(self):
        return f'{self.name} - {self.department}'

    @property
    def updated_date(self):
        return self.lessons.all().latest('updated_date').updated_date if self.lessons.exists() else None


class Teacher(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    patronymic = models.CharField(max_length=70)
    universities = models.ManyToManyField(University, related_name='teachers')

    class Meta:
        db_table = 'teachers'
        ordering = ('surname',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'surname', 'patronymic'],
                name='unique_teacher',
            )
        ]

    def __str__(self):
        return f'{self.short_name}'

    @property
    def full_name(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    @property
    def short_name(self):
        return f'{self.surname} {self.name[0]}. {self.patronymic[0]}.'


class Subject(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, related_name='subjects', on_delete=models.CASCADE)

    class Meta:
        db_table = 'subjects'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'university'],
                name='unique_subject_in_university',
            )
        ]

    def __str__(self):
        return f'{self.name} - {self.university}'


class AcademyBuilding(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, related_name='academy_buildings', on_delete=models.CASCADE)

    class Meta:
        db_table = 'academy_buildings'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'university'],
                name='unique_academy_building_in_university',
            )
        ]

    def __str__(self):
        return f'{self.name} - {self.university.name}'


class Auditorium(models.Model):
    name = models.CharField(max_length=10)
    academy_building = models.ForeignKey(AcademyBuilding, related_name='auditoriums', on_delete=models.CASCADE)

    class Meta:
        db_table = 'auditoriums'
        ordering = ('-id',)
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'academy_building'],
                name='unique_auditorium_in_academy_building',
            )
        ]

    def __str__(self):
        return f'{self.name} - {self.academy_building.name} - {self.academy_building.university.name}'


class Lesson(models.Model):
    LECTURE = 0  # Лекція
    PRACTICAL = 1  # Практична
    LAB = 2  # Лабораторна
    SEMINAR = 3  # Семінар
    LESSON_TYPES = (
        (LECTURE, 'Lecture'),
        (PRACTICAL, 'Practical'),
        (LAB, 'Lab'),
        (SEMINAR, 'Seminar'),
    )

    WHOLE_GROUP = 0
    SUBGROUP_1 = 1
    SUBGROUP_2 = 2
    SUBGROUP_TYPES = (
        (WHOLE_GROUP, 'Whole group'),
        (SUBGROUP_1, 'Subgroup 1'),
        (SUBGROUP_2, 'Subgroup 2'),
    )

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    WEEK_DAYS = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )

    lesson_number = models.PositiveSmallIntegerField(
        help_text='lesson number in schedule (first lesson, etc.)',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    type = models.PositiveSmallIntegerField(choices=LESSON_TYPES, help_text='e.g. lecture/lab/seminar/etc. lesson')
    subgroup = models.PositiveSmallIntegerField(
        help_text='group could divides on a few parts for some lessons',
        choices=SUBGROUP_TYPES
    )
    week_day = models.PositiveSmallIntegerField(choices=WEEK_DAYS)
    lesson_url = models.URLField(
        help_text='url to connect to the lesson in google meet/zoom',
        max_length=500,
        blank=True,
        null=True,
    )
    frequency = models.PositiveSmallIntegerField(
        choices=Frequency.LESSON_FREQUENCY,
        default=Frequency.WEEKLY,
        help_text='indicates how often the lesson occurs (every week or once in 2 weeks)'
    )
    additional_info = models.CharField(max_length=70, blank=True, null=True)

    teachers = models.ManyToManyField(Teacher, related_name='lessons')
    groups = models.ManyToManyField(Group, related_name='lessons')
    subject = models.ForeignKey(Subject, related_name='lessons', on_delete=models.RESTRICT)
    auditorium = models.ForeignKey(Auditorium, related_name='lessons', on_delete=models.RESTRICT)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lessons'
        ordering = ('id',)

    def __str__(self):
        return f'{self.lesson_number}. {self.subject.name} - ' \
               f'{",".join([teacher.short_name for teacher in self.teachers.all()])} - ' \
               f'{",".join([group.name for group in self.groups.all()])}'
