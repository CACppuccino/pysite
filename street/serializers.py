from rest_framework import serializers
from django.contrib.auth.models import User
from .models import lost_street, ls_gallery, ls_comments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ls_index_serializer(serializers.ModelSerializer):
    class Meta:
        model = lost_street
        fields = ['id','name','cover']

class ls_gallery_serializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField('thumbnail')  # cannot solve thumbnail problem
    class Meta:
        model = ls_gallery
        fields = '__all__'

class ls_comments_serializer(serializers.ModelSerializer):
    #uname = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    uname = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = ls_comments
        fields = ('uname', 'time', 'content',) # sname is removed here since the serializer will only be used for read
        
class ls_street_info(serializers.ModelSerializer):
    gallery = ls_gallery_serializer(many=True)
    comments = ls_comments_serializer(many=True)
    class Meta:
        model = lost_street
        fields = ['id','name','cover','intro','gallery','comments']

