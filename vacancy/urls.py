from django.urls import path

from vacancy.views import VacancyListCreateView, VacancyRetrieveUpdateDeleteAPIView


urlpatterns = [
    path("", VacancyListCreateView.as_view(), name="vacancy_list_create"),
    path("<slug:slug>/", VacancyRetrieveUpdateDeleteAPIView.as_view(), name="vacancy_detail")
]