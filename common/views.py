from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from common.models import Experience
from common.serializers import ExperienceListSerializer, ExperienceCreateSerializer


# Create your views here.
class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ExperienceCreateSerializer
        return ExperienceListSerializer


class ExperienceRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ExperienceCreateSerializer
        return ExperienceListSerializer
