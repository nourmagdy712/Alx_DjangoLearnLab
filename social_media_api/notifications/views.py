from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notifications.models import Notification
from django.contrib.auth.models import User
from rest_framework import permissions, status

# Create your views here.


class FollowNotificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        follower = request.user
        followed = User.objects.get(pk=pk)

        # Create a notification when a user follows another user
        notification = Notification.objects.create(
            recipient=followed,
            actor=follower,
            verb=f"{follower.username} started following you",
            target=follower
        )

        return Response({"detail": "Followed successfully."}, status=status.HTTP_201_CREATED)

class GetNotificationsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        # Here, you can serialize notifications or return as is.
        return Response({"notifications": notifications}, status=status.HTTP_200_OK)