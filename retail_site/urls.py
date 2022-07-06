from django.urls import path

from retail_site.views import LessonsAPIView, GroupTeachersAPIView, GroupSubjectsAPIView, UniversityAPIView, \
    DepartmentAPIView, GroupAPIView

app_name = 'retail'

urlpatterns = [
    path('universities/', UniversityAPIView.as_view(), name='universities'),
    path('universities/<int:university_id>/departments/', DepartmentAPIView.as_view(), name='departments'),
    path('departments/<int:department_id>/groups/', GroupAPIView.as_view(), name='groups'),

    path('groups/<int:group_id>/lessons/', LessonsAPIView.as_view(), name='group-lessons'),
    path('groups/<int:group_id>/teachers/', GroupTeachersAPIView.as_view(), name='group-teachers'),
    path('groups/<int:group_id>/subjects/', GroupSubjectsAPIView.as_view(), name='group-subjects'),
]
