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


class VacancytRetrieveView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


class VacancytUpdateView(generics.UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer


class VacancyDeleteView(generics.DestroyAPIView):
    queryset = Vacancy.objects.all()


class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return VacancyCreateSerializer
        return VacancyListSerializer
