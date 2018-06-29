from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import doc_street
from .serializers import StreetListSerializer

# Create your views here.

class StreetList(APIView):

    def get(self, request, format=None):
        slist = doc_street.objects.filter(status='permit')        
        serializer = StreetListSerializer(slist, many=True)
        return Response(serializer.data)
