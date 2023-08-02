from django.db import models

from common.models import Skills
from company.models import Company


class Vacancy(models.Model):
    class LevelType(models.TextChoices):
        JUNIOR = "Junior"
        MIDDLE = "Middle"
        SENIOR = "Senior"

    class JobType(models.TextChoices):
        FULL_TIME = "Full time"
        PART_TIME = "Part time"
        HYBRID = "Hybrid"

    title = models.CharField(max_length=255)
    experience = models.TextField(max_length=255)
    job_type = models.CharField(max_length=255, choices=JobType.choices, default=JobType.FULL_TIME)
    level = models.CharField(max_length=255, choices=LevelType.choices, default=LevelType.JUNIOR)
    salary = models.FloatField(default=0)
    overview = models.CharField(max_length=255)
    description = models.TextField(255)
    offer = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_vacancy')
    skills = models.ManyToManyField(Skills)
