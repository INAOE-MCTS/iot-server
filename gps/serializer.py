from django.db import models
from rest_framework import serializers
from .models import GpsModel, DataModel


class GpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpsModel
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'
