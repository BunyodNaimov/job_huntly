from django.contrib import admin
from .models import Company, CompanyBenefit, Benefit

admin.site.register(Company)
admin.site.register(Benefit)
admin.site.register(CompanyBenefit)
