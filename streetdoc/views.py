from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import doc_street, doc_building
from .serializers import StreetListSerializer, StreetInfoSerializer, BuildingInfoSerializer
from django.core.exceptions import ObjectDoesNotExist 
from copy import deepcopy

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
            # `pbuild` is to record not permited builidng info
            pbuild = []
            for x in buildings:
                flag = False
                for key, value in x.items():
                    if key=='status' and value!='permit':
                        flag = True
                        break
                if flag:
                    # remove is may bring concurrent modification problem
                    pbuild.append(x)
            # cannot assign the value directly to the serializer.data??? 
            # so record and remove is the only choice
            for x in pbuild:
                buildings.remove(x)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class BuildingInfo(APIView):
    """
    API return/procced the building HTML content
    """
    
    def get(self, request, format=None):
        bid = request.query_params.get('bid', None)
        if bid:
            try:
                building_info = doc_building.objects.get(id=bid) 
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = BuildingInfoSerializer(building_info)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) # if there is no bid

    def post(self, request, format=None):
        building = request.data['building']
        if request.user.is_authenticated(): 
            user = request.user
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if building:
            try:
                oldb = doc_building.objects.get(id=building['id'])
            except ObjectDoesNotExist:
                return Response('no builidng exist', status=status.HTTP_400_BAD_REQUEST)
            #newb = doc_building(name=building['name'], cover=)
           # newb = oldb
            newb = deepcopy(oldb)
            newb.author = user
            newb.status = "waiting"
            newb.intro = building['intro']
            newb.id = None
            newb.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
