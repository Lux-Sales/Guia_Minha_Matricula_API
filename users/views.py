from rest_framework import viewsets, permissions, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView

class UserViewSet(APIView):
    def get(self, request):
        return Response({"message":"success!"}, status=status.HTTP_200_OK)