from rest_framework import serializers
from app1.models import Jokes

class Jokes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Jokes
        fields = ['id', 'content', 'date']
