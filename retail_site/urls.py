from django.urls import path

from retail_site.views import GroupLessonsAPIView

app_name = 'retail'

urlpatterns = [
    path('group/<int:group_id>/schedule/', GroupLessonsAPIView.as_view(), name='schedule'),
]
