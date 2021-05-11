from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import AddUserSerializer 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

class RegisterUserViewSet(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        add_user_serializer = AddUserSerializer(data=request.data)
        if add_user_serializer.is_valid(self):
           response = add_user_serializer.save()
           return response

class LoginViewSet(APIView):
    permission_classes = [AllowAny]    

    def post(self, request, format=None):
        user = authenticate(username=request.data['email'], password=request.data['password'])
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access':str(refresh.access_token), 'id':user.id}, status= status.HTTP_200_OK)
        else: 
            return Response('Invalid email or password', status=status.HTTP_401_UNAUTHORIZED)