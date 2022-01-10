# This is our serializer page
from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class PatientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Patient
		fields = ('id', 'url', 'name', 'Symptom1', 'Symptom2')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user