from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(unique=True, max_length=255, null=True, blank=True)
    phone = models.PositiveIntegerField(max_length=15, null=True, blank=True)

    USERNAME_FIELD = "email"
