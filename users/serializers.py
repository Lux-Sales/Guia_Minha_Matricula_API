from rest_framework import serializers
from users.models import User
from rest_framework.response import Response
from rest_framework import status

class AddUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200,required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=200,required=True)
    is_teacher = serializers.BooleanField(required=False, allow_null=True, default=False)

    def create(self, validated_data):
        if(validated_data['email'].find('@aluno.unb.br') > 0 or validated_data['email'].find('@unb.br') > 0):
            if(validated_data['is_teacher']):
                user = User.objects.create(first_name=validated_data['first_name'], last_name=validated_data['last_name'], email=validated_data['email'], username=validated_data['email'], is_teacher="True")
            else:
                user = User.objects.create(first_name=validated_data['first_name'], last_name=validated_data['last_name'], email=validated_data['email'], username=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            return Response({"message":"User created"}, status=status.HTTP_201_CREATED)
        return Response({"message":"Invalid email"}, status=status.HTTP_400_BAD_REQUEST)
