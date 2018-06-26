from rest_framework import serializers
from .models import lost_street, ls_gallery, ls_comments

class ls_index_serializer(serializers.ModelSerializer):
    class Meta:
        model = lost_street
        fields = ['id','name','cover']

class ls_street_info(serializers.ModelSerializer):
    gallery = serializers.StringRelatedField(many=True) 
    class Meta:
        model = lost_street
        fields = ['id','name','cover','intro','gallery']
