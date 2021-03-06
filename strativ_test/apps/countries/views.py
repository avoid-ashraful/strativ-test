from django.http import HttpResponse
from django.template import loader
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from strativ_test.apps.countries.filters import CountryFilter
from strativ_test.apps.countries.models import Country
from strativ_test.apps.countries.serializers import CountrySerializer, CountryDetailsSerializer


class CountryListAPIView(ListCreateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter
    pagination_class = None  # Removing this line will activate default pagination
    permission_classes = [IsAuthenticated]


class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CountryDetailsSerializer
    queryset = Country.objects.all()
    permission_classes = [IsAuthenticated]


def country_list(request):
    template = loader.get_template('country_list.html')
    return HttpResponse(template.render({}, request))


def country_details(request):
    template = loader.get_template('country_details.html')
    return HttpResponse(template.render({}, request))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))
