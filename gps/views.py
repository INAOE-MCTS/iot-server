from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from .serializer import DataSerializer


class Index(APIView):
    def get(self, request):
        numero = random.randint(1, 255)
        return Response({'Random': numero})

    def post(self, request):
        data = request.data
                                                
        serializer = DataSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(data)
        actuador = random.randint(1, 255)
        return Response( actuador , status=status.HTTP_200_OK)