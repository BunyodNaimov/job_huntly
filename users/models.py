from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(unique=True, max_length=255, null=True, blank=True)
    phone = models.PositiveIntegerField(max_length=15, null=True, blank=True)

    USERNAME_FIELD = "email"


class Employee(models.Model):
    user_id = models.ForeignKey(CustomUser)
    region = models.CharField(max_length=256, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=50, default="male")


class Skills(models.Model):
    name = models.CharField(unique=False, max_length=255, null=False)


class Experience(models.Model):
    class TypeChoice(models.TextChoices):
        PART_TIME = "Part time"
        FULL_TIME = "Full time"
        HYBRID = "Hybrid"

    title = models.CharField(unique=True, max_length=255, null=False)
    employee_id = models.ForeignKey(Employee)
    company_id = models.ForeignKey(Company)
    from_a = models.CharField(unique=False, max_length=255, null=False)
    to = models.CharField(unique=False, max_length=255, null=False)
    type = models.CharField(max_length=50, choices=TypeChoice.choices)
    description = models.TextField(max_length=500, null=True)
    skills = models.ForeignKey(Skills)
