from django.urls import path
from .views import UserSearchView, SendFriendRequestView, ManageFriendRequestView, ListFriendsView, ListPendingFriendRequestsView, SignupView, CustomAuthToken

urlpatterns = [
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/send/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friend-request/manage/<int:request_id>/<str:action>/', ManageFriendRequestView.as_view(), name='manage-friend-request'),
    path('friends/', ListFriendsView.as_view(), name='list-friends'),
    path('friend-requests/pending/', ListPendingFriendRequestsView.as_view(), name='list-pending-requests'),
    path('signup/', SignupView.as_view(), name='signup'),  # Signup endpoint
    path('login/', CustomAuthToken.as_view(), name='login'),  # Login endpoint
]
