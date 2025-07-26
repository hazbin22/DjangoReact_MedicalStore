from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

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
    
class Profile(models.Model):
    # Change User to settings.AUTH_USER_MODEL
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile') # <--- CHANGE THIS LINE
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.email} Profile'

# Signals to automatically create/update Profile when a User is created/updated
# Change sender=User to sender=settings.AUTH_USER_MODEL
@receiver(post_save, sender=settings.AUTH_USER_MODEL) # <--- CHANGE THIS LINE
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL) # <--- CHANGE THIS LINE
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()