from django.urls import path

from retail_site.views import GroupLessonsAPIView, GroupTeachersAPIView, GroupSubjectsAPIView

app_name = 'retail'

urlpatterns = [
    path('group/<int:group_id>/schedule/', GroupLessonsAPIView.as_view(), name='group-schedule'),
    path('group/<int:group_id>/teachers/', GroupTeachersAPIView.as_view(), name='group-teachers'),
    path('group/<int:group_id>/subjects/', GroupSubjectsAPIView.as_view(), name='group-subjects'),
]
