from django.db import models
from rest_framework import serializers
from .models import DataModel


class GpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'
