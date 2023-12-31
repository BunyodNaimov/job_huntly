from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework import generics
from vacancy.models import Vacancy
from vacancy.serializers import VacancyCreateSerializer, VacancyListSerializer


class VacancyListCreateView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return VacancyCreateSerializer
        return VacancyListSerializer


class VacancyRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return VacancyCreateSerializer
        return VacancyListSerializer
