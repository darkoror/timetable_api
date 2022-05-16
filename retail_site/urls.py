from django.urls import path

from retail_site.views import ScheduleAPIView

app_name = 'retail'

urlpatterns = [
    path('group/<int:group_id>/', ScheduleAPIView.as_view(), name='schedule'),
]
