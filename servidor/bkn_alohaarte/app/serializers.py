from rest_framework import serializers
from app.models import Properties, Users

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ['id', 'title', 'description']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'firstname', 'lastname', 'email', 'password']