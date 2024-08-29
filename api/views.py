from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
from datetime import timedelta

from .models import CustomUser, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import SignupSerializer

User = get_user_model()

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        keyword = self.request.query_params.get('q', None)
        if keyword:
            return User.objects.filter(Q(email__iexact=keyword) | Q(username__icontains=keyword))
        return User.objects.none()

class SendFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        to_user_email = request.data.get('email')
        if not to_user_email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            to_user = User.objects.get(email__iexact=to_user_email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user == to_user:
            return Response({"error": "You cannot send a friend request to yourself"}, status=status.HTTP_400_BAD_REQUEST)

        if FriendRequest.objects.filter(from_user=request.user, to_user=to_user).exists():
            return Response({"error": "Friend request already sent"}, status=status.HTTP_400_BAD_REQUEST)

        # Check rate limit
        one_minute_ago = timezone.now() - timedelta(minutes=1)
        recent_requests_count = FriendRequest.objects.filter(from_user=request.user, timestamp__gte=one_minute_ago).count()

        if recent_requests_count >= 3:
            return Response({"error": "You cannot send more than 3 friend requests in a minute"}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        friend_request = FriendRequest.objects.create(from_user=request.user, to_user=to_user, status='pending')
        return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_201_CREATED)

class ManageFriendRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, request_id, action):
        try:
            friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user, status='pending')
        except FriendRequest.DoesNotExist:
            return Response({"error": "Friend request not found"}, status=status.HTTP_404_NOT_FOUND)

        if action == 'accept':
            friend_request.status = 'accepted'
            friend_request.save()
        elif action == 'reject':
            friend_request.status = 'rejected'
            friend_request.save()
        else:
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_200_OK)

class ListFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        accepted_requests = FriendRequest.objects.filter(Q(from_user=self.request.user) | Q(to_user=self.request.user), status='accepted')
        friends_ids = {req.from_user.id if req.to_user == self.request.user else req.to_user.id for req in accepted_requests}
        return User.objects.filter(id__in=friends_ids)

class ListPendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')


# User Signup View
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Custom Login View
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '').lower()
        password = request.data.get('password', '')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
