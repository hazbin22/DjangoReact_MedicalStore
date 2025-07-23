# medical_store/Pharmio/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Import settings
from django.conf.urls.static import static # Import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')), # Assuming you have cart urls
    path('orders/', include('orders.urls')), # Assuming you have orders urls
    path('accounts/', include('accounts.urls')), # Assuming you have accounts urls for any non-API user views
    path('users/', include('users.urls')), # Your existing users app urls
]

# Add this for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)