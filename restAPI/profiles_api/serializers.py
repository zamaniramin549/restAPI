from rest_framework import serializers
from .models import User

class HelloSerializer(serializers.Serializer):
    first_name= serializers.CharField(max_length= 10)
    email= serializers.EmailField()
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style':{'input_type': 'password'}
            }
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password'],
        )
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
    