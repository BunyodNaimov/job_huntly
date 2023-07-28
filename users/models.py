from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(unique=True, max_length=255, null=True, blank=True)
    phone = models.PositiveIntegerField(max_length=15, null=True, blank=True)

    USERNAME_FIELD = "email"

class Employee(models.Model):
    class GenderChoises(models.TextChoices):
        MALE = "male"
        FEMALE = "female"



    user_id = models.ForeignKey(CustomUser)
    region = models.CharField(max_length=256, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=50, choices=GenderChoises.choices)