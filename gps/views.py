from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from .serializer import GpsSerializer, DataSerializer
from .models import DataModel, GpsModel

class GpsView(APIView):
    def get(self, request):
        gps = GpsModel.objects.all()
        serializer = GpsSerializer(gps, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data         
        serializer = GpsSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(data)
        return Response(status=status.HTTP_200_OK)


class DataView(APIView):
    def get(self, request):
        data = DataModel.objects.all()
        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data                        
        serializer = DataSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(data)
        actuador = random.randint(1, 255)
        return Response( actuador , status=status.HTTP_200_OK)