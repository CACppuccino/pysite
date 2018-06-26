from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import basicUser

# Create your views here.

class UserList(APIView):
    """
    A trail for the user list api
    """
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,) 
    """
    def get(self, request, format=None):
        usr = User.objects.all()
        serializer = basicUser(usr, many=True)
        return Response(serializer.data)

class usrValidate(APIView):
    """
    for validation of the user
    """
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        return Response('wrong method')

    def post(self, request, format=None):
        uname = request.data.get('username', None)
        pwd = request.data.get('password', None)
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return Response('authenticatiion succeed')    
        return Response('authentication failed')

class usrRigister(APIView):
    """
    for user registeration
    """
    def post(self, request, format=None):
        print(request.data)
        
        return Response('ok') 

@api_view(['GET'])
def repeat_user(request):
    if request.method == 'GET':
        uname = request.GET.get('username', None)
        if uname and not User.objects.filter(username=uname).exists():
            return Response('pass')
        else:
            return Response('denied')
    return Response('wrong method', status = status.HTTP_400_BAD_REQUEST)  
