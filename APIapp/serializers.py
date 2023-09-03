from rest_framework import serializers
from APIapp.models import UserProfile

class HelloSerializer(serializers.Serializer):
    """ Creating Serializers a name field for testing API view """
    name = serializers.CharField(max_length=10)