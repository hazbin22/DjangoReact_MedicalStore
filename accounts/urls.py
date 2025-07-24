# medical_store/accounts/urls.py

from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserLogoutAPIView,
    ProtectedView,
    # UserLoginAPIView is removed as TokenObtainPairView handles login
)
from rest_framework_simplejwt.views import TokenBlacklistView # Keep for specific blacklisting endpoint if needed

app_name = 'accounts' # This is good!

urlpatterns = [
    # --- Custom User Management API Endpoints ---
    path('register/', UserRegistrationAPIView.as_view(), name='user_register'),
    # No need for a separate 'api/login/' path if using api/token/ from Pharmio/urls.py for login

    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'), # Your custom logout
    path('protected/', ProtectedView.as_view(), name='protected_view'), # Your protected test view

    # You can keep TokenBlacklistView here if you want a dedicated endpoint for blacklisting a token manually
    # path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # Note: Your UserLogoutAPIView already calls token.blacklist(), so this direct view might be redundant for normal logout flow.
]