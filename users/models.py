from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)

    # Remove the redundant username field if you don’t need to override it
    # username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    def __str__(self):
        # Safely return name or email (if name is not available)
        return self.name if self.name else self.email

    def save(self, *args, **kwargs):
        # Automatically set username to email if it's not provided
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)