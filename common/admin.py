from django.contrib import admin

from .models import Education, Experience, Employee

admin.site.register(Employee)
admin.site.register(Experience)
admin.site.register(Education)
