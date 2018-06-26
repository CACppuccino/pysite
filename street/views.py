from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import lost_street, ls_gallery, ls_comments
from .serializers import ls_index_serializer, ls_street_info
from rest_framework.response import Response
from rest_framework import authentication, permissions, status# turn off during debug and dev
from rest_framework.views import APIView

# Create your views here.

class index_page(APIView):
    """
    for the lost street index page api
    """
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    def get(self, request, format=None):
        """
        return the name, cover of the lost street 
        """
        streets = lost_street.objects.all()
        serializer = ls_index_serializer(streets, many = True)
        return Response(serializer.data)

class street_page(APIView):
    """
    for illustrating the street info  
    """
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    def get(self, request, format=None):
        """
        param: id
        return the id,name,cover,intro and gallery(thumbnail in the future)
        """
        street_id = request.GET.get('sid', None)
        if street_id:
            try:
                street = lost_street.objects.get(id = street_id)
            except ObjectDoesNotExist:
                return Response('no matching record', status = status.HTTP_400_BAD_REQUEST)
            serializer = ls_street_info(street)
            return Response(serializer.data)
        return Response('no matching record', status = status.HTTP_400_BAD_REQUEST)
