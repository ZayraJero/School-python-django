from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BootcampSerializer, KoderSerializer
from .models import Bootcamp, Koder

# Create your views here.


class BootcampViewSet(viewsets.ModelViewSet):

    queryset = Bootcamp.objects.all().order_by("name")
    serializer_class = BootcampSerializer


class KoderViewSet(viewsets.ModelViewSet):

    queryset = Koder.objects.all().order_by("full_name")
    serializer_class = KoderSerializer