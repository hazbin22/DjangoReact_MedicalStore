# medical_store/accounts/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Removed UserLoginSerializer as UserLoginAPIView is being removed
from .serializers import UserRegistrationSerializer # Only need UserRegistrationSerializer now
# Removed authenticate as UserLoginAPIView is being removed
# from django.contrib.auth import authenticate

class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny] # Allow anyone to register

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate tokens upon successful registration is a good idea for immediate login
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User registered successfully',
                'user_id': user.id,
                'email': user.email,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- REMOVED: UserLoginAPIView ---
# You will now use the standard JWT endpoint at /api/token/ for login.
# This simplifies your code and leverages the robust simplejwt implementation.

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated] # Only authenticated users can logout

    def post(self, request):
        try:
            # Get the refresh token from the request data
            # The client should send the refresh token in the body for logout
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist() # Blacklist the refresh token

            return Response({'message': 'Logout successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            # Handle cases where refresh token is missing or invalid
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Example of a protected view for testing
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated] # Requires a valid JWT to access

    def get(self, request):
        # request.user is available because of JWTAuthentication in settings.py
        return Response({'message': f'Welcome, {request.user.email}! You are authenticated.'}, status=status.HTTP_200_OK)