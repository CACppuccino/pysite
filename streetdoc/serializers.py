from rest_framework import serializers
from .models import doc_street

class StreetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = doc_street
        fields = ('id', 'name', 'cover')
