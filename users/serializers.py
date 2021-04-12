from rest_framework import serializers
from users.models import User

class AddUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        if(validated_data['email'].find('@aluno.unb.br') > 0 or validated_data['email'].find('@unb.br') > 0):
            user = User.objects.create(first_name=validated_data['first_name'], last_name=validated_data['last_name'], email=validated_data['email'], username=validated_data['email'])
            user.set_password(validated_data['password'])
            user.save()
            return {'message':'User has been created'} 
        return {'message':'Invalid Email'}
