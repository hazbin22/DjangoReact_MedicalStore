from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, ProtectedView # Import your views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # Used by default for login (gets access and refresh tokens)
    TokenRefreshView,    # Used to get a new access token using a refresh token
    TokenBlacklistView,
)

app_name = 'accounts' # Use the correct app_name for each app

urlpatterns = [
     # JWT standard endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Standard login endpoint (gives access + refresh)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Standard refresh endpoint
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # Our custom user management API endpoints
    path('api/register/', UserRegistrationAPIView.as_view(), name='user_register'),
    path('api/login/', UserLoginAPIView.as_view(), name='user_login'), # This is your custom login view
    path('api/logout/', UserLogoutAPIView.as_view(), name='user_logout'),

    # Example protected endpoint
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),
]