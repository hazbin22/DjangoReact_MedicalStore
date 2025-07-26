# medical_store/accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser, Profile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2') # Only expose email for registration

    def validate(self, data):
        # Check if passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        # Create a new user instance
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    # No create or update methods needed as this serializer is for input validation only

class ProfileSerializer(serializers.ModelSerializer):
    # We can also include the user's email directly in the profile serializer
    # This makes it easier for the frontend to display
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = [
            'id', # Primary key for the profile
            'user', # The foreign key to the CustomUser (you might not send this from frontend)
            'email', # User's email (read-only)
            'phone_number',
            'address',
            'city',
            'state',
            'zip_code',
            'profile_picture',
            'date_of_birth'
        ]
        read_only_fields = ['user', 'email'] # User and email should typically not be updated via the profile endpoint

class CustomUserSerializer(serializers.ModelSerializer):
    # Nested serializer for the profile
    profile = ProfileSerializer(read_only=True) # Ensure this matches the related_name in OneToOneField

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'profile'] # Include 'profile' here
        read_only_fields = ['email'] # Email is read-only for existing users via this serializer