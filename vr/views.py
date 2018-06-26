from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# Create your views here.

@api_view(['GET'])
def version(request):
    """
    returns the version and download link
    """
    data = dict(version=0.03,link='http://127.0.0.1:8000/static/files/haha.txt')
    return Response(data)
