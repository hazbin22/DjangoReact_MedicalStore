# medical_store/accounts/urls.py

from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserLogoutAPIView,
    ProtectedView,
    UserProfileView, # Import the new view
    UserDetailView,
)
from rest_framework_simplejwt.views import TokenBlacklistView # Keep for specific blacklisting endpoint if needed

app_name = 'accounts' # This is good!

urlpatterns = [
    # --- Custom User Management API Endpoints ---
    path('register/', UserRegistrationAPIView.as_view(), name='user_register'),
    # No need for a separate 'api/login/' path if using api/token/ from Pharmio/urls.py for login

    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'), # Your custom logout
    path('protected/', ProtectedView.as_view(), name='protected_view'), # Your protected test view

    # New URL for getting/updating user's own profile
    path('profile/', UserProfileView.as_view(), name='user_profile'),

    # New URL for getting user's full details (including nested profile)
    path('me/', UserDetailView.as_view(), name='user_detail'), # 'me' is a common convention for current user details
]