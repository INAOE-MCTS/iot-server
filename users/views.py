from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from rest_framework import status
from django.contrib.auth.models import User
from crypto import descipher_asimetric, descipher_simetric, session_key


#Serializers
from .serializers import (
    UserSerializer,
    )

# Models
from .models import (
    User,
)

# Vista para crear Usuarios
class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        email = data['email']
        user = User.objects.filter(email=email).first()
        serializer = UserSerializer(data = data)
        
        if user is None:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response({"message": "El usuario ya existe"}, status=status.HTTP_226_IM_USED)


# Vista para el login
class LoginView(APIView):
    def post(self, request):
        print("request: ", request.data)
        print("aplicamos el algoritmo de descifrado")
        print(request.data['ciphertext'])
        print(request.data['iv'])
        print(session_key)
        # data = descipher_asimetric(request.data)
        data = descipher_simetric(request.data['ciphertext'], request.data['iv'], session_key)
        print("request_plain: ", data)

        print(data.data)
        email = data.data['email']
        password = data.data['password']
        public_key_cipher = data.data['public_key']
        


        # Busca el email en la BD y almacena la informacion en user.
        user = User.objects.filter(email=email).first()
        print(user)

        # Si no existe, devuelve error de autentificacion al response del usuario
        if user is None:
            raise AuthenticationFailed("El usuario no existe!")
        
        # Si existe user, verifica la contraseña, si es incorrecta devuelve error de autentificacion al response del usuario
        if not user.check_password(password):
            raise AuthenticationFailed("Contrasena incorrecta!")

        # JWT encripta el id y envia token al cliente.
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response(data={'token': token}, status=status.HTTP_200_OK)