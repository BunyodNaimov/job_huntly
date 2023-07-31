from django.db import models
from users.models import CustomUser


class Sector(models.Model):
    name = models.CharField(unique=True, max_length=255)


class Company(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(unique=True, max_length=255)
    region = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    size = models.IntegerField()
    revenue = models.CharField(max_length=255)
    found_year = models.DateField()
    logo = models.ImageField(null=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name="companies")
    
    def __str__(self):
        return self.name


class Benefit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(null=True)


class CompanyBenefit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="benefits")
    benefit = models.ForeignKey(Benefit, on_delete=models.CASCADE, related_name="companies")
