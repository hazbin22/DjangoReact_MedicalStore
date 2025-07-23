from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
    # Override create_user to use email as the main identifier
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        # Ensure username is handled; it can be None if it's optional in your model
        # You can set it to None, or even generate a unique one if you desire
        # For now, let's pass None if it's not provided, aligning with your model's nullable username
        extra_fields.setdefault('username', None) # Explicitly set username to None
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Override create_superuser to use email as the main identifier
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # Ensure username is handled for superuser as well, if it's expected
        extra_fields.setdefault('username', None) # Explicitly set username to None for superuser too

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields) # Call our custom create_user

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=False, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # No other fields are strictly required besides USERNAME_FIELD and password

    objects = CustomUserManager()

    def __str__(self):
        return self.email