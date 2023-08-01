from rest_framework import serializers

from vacancy.models import Vacancy


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ["id", "title", "experience", "level", "job_type", "salary", "overview", "description", "offer"]


class VacancyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ["id", "title", "experience", "level", "job_type", "salary", "overview", "description", "offer"]
        read_only_fields = ("id",)
