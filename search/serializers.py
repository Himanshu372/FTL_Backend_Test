from rest_framework import serializers
from search.models import corpusData


# Serializer for the corpusData model
class corpusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = corpusData
        fields = ['token', 'token_count']




