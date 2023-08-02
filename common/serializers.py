from rest_framework import serializers

from common.models import Experience


class ExperienceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["id", "title", "employee", "company", "from_a", "to", "type", "description", "skills"]


class ExperienceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["id", "title", "employee", "company", "from_a", "to", "type", "description", "skills"]
        read_only_fields = ("id",)
