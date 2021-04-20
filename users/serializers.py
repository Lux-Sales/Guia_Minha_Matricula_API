from rest_framework import serializers, status
from users.models import User
from rest_framework.response import Response

class AddUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200,required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=200,required=True)

    def create(self, validated_data):
        if(validated_data['email'].find('@aluno.unb.br') > 0 or validated_data['email'].find('@unb.br') > 0):
            user = User.objects.create(first_name=validated_data['first_name'], last_name=validated_data['last_name'], email=validated_data['email'], username=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            return 'User has been created'
        return 'Invalid Email'
