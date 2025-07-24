# medical_store/Pharmio/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import standard JWT views HERE (project-level)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # For getting access and refresh tokens (main login)
    TokenRefreshView,     # For refreshing access tokens
    TokenVerifyView,      # For verifying access tokens (optional but useful)
    # TokenBlacklistView is usually used within an app's urls or via a custom logout view,
    # so we won't put it here directly.
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include app-specific URLs
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')), # This will include your custom account URLs
    path('users/', include('users.urls')), # Assuming this is for user profiles etc.

    # --- JWT Authentication Endpoints (Standard, project-level) ---
    # This is the primary endpoint your frontend will hit for login.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)