from rest_framework import serializers

from vacancy.models import Vacancy


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ["id", "title", "experience", "level", "job_type", "salary", "overview", "description", "offer"]


class VacancyCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Vacancy
        fields = ["title", "experience", "level", "job_type", "salary", "overview", "description", "offer"]
