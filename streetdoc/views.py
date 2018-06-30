from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import doc_street
from .serializers import StreetListSerializer, StreetInfoSerializer

# Create your views here.

class StreetList(APIView):

    """
    List the street general info API
    """
    def get(self, request, format=None):
        slist = doc_street.objects.filter(status='permit')        
        serializer = StreetListSerializer(slist, many=True)
        return Response(serializer.data)

class StreetInfo(APIView):

    def get(self, request, format=None):
        sid = request.query_params.get('sid', None)
        if sid:
            try:
               street_info = doc_street.objects.get(id=sid)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = StreetInfoSerializer(street_info)
            # remove the element of unpermitted
            buildings = serializer.data['buildings']
            for x in buildings:
                flag = False
                for key, value in x.items():
                    if key=='status' and value!='permit':
                        flag = True
                        break
                if flag:
                    buildings.remove(x)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
