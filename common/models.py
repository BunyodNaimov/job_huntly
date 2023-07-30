from django.db import models

from users.models import CustomUser


class Employee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_employee')
    region = models.CharField(max_length=256, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, default="male")


class Skills(models.Model):
    name = models.CharField(unique=False, max_length=255, null=False)


class Experience(models.Model):
    class TypeChoice(models.TextChoices):
        PART_TIME = "Part time"
        FULL_TIME = "Full time"
        HYBRID = "Hybrid"

    title = models.CharField(unique=True, max_length=255, null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_experience')
    # company = models.ForeignKey(Company, )
    from_a = models.CharField(unique=False, max_length=255, null=False)
    to = models.CharField(unique=False, max_length=255, null=False)
    type = models.CharField(max_length=50, choices=TypeChoice.choices)
    description = models.TextField(max_length=500, null=True)
    skills = models.ForeignKey(
        Skills, on_delete=models.CASCADE, choices=TypeChoice.choices, default=TypeChoice.FULL_TIME
    )
