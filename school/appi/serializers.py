from rest_framework import serializers

from .models import Bootcamp, Koder


class BootcampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = "__all__"


class KoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Koder
        fields = "__all__"
