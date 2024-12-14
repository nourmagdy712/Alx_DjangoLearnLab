from django.urls import path
from notifications.views import FollowNotificationView, GetNotificationsView

urlpatterns = [
    path('follow/<int:pk>/', FollowNotificationView.as_view(), name='follow-notification'),
    path('notifications/', GetNotificationsView.as_view(), name='get-notifications'),
]