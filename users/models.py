from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(blank=True, max_length=255, unique=True)
    password = models.CharField(max_length=255)
    public_key = models.CharField(max_length=1055, blank=True, null=True)
    session_key = models.CharField(max_length=1055, blank=True, null=True)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.email}"
