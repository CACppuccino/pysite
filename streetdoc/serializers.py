from rest_framework import serializers
from .models import doc_street, doc_building

class StreetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = doc_street
        fields = ('id', 'name', 'cover')

class BuildingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = doc_building
        fields = ('id', 'name', 'cover', 'status')

class StreetInfoSerializer(serializers.ModelSerializer):
    buildings = BuildingListSerializer(many=True)
    class Meta:
        model = doc_street
        fields = '__all__'

class BuildingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = doc_building
        fields = '__all__'
