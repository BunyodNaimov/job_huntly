from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=355)
    experience = models.TextField(max_length=255)
    level = models.CharField(max_length=15, help_text="Junior | Middle | Senior")
    job_type = models.CharField(max_length=15, help_text="full time | part time")
    salary = models.FloatField(default=0)
    overview = models.CharField(max_length=455)
    description = models.TextField(255)
    offer = models.TextField()
    # company = models.ForeignKey(on_delete=models.CASCADE, related_name='company_vacancy')
    # skills = models.ManyToManyField()