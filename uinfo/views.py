from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User 
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from .serializers import BasicUserSerializer, UserInfoSerializer, UserSerializer
from .models import UserInfo

# Create your views here.

class UserList(APIView):
    """
    A trail for the user list api
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,) 
    def get(self, request, format=None):
        if request.user.is_authenticated():
            usr = request.user
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            uinfo = UserInfo.objects.get(user=usr)
        except ObjectDoesNotExist:
            uinfo = UserInfo(user=usr)
            uinfo.save()
            serializer = UserInfoSerializer(uinfo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer = UserInfoSerializer(uinfo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        if request.user.is_authenticated():
            usr = request.user
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            uinfo = UserInfo.objects.get(user=usr)
        except ObjectDoesNotExist:
            # create the userinfo model for the new user
            uinfo = UserInfo(user=usr, organization=request.data['organization'], summary=request.data['summary'])
            uinfo.save()
            return Response(status=status.HTTP_201_CREATED)
        uinfo.organization = request.data['organization']
        uinfo.summary = request.data['summary']
        uinfo.save()
        usr.email = request.data['email']
        usr.save()
        return Response(status=status.HTTP_202_ACCEPTED)

class usrValidate(APIView):
    """
    for validation of the user
    """
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        uname = request.data.get('username', None)
        pwd = request.data.get('password', None)
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return Response('authenticatiion succeed')    
        return Response('authentication failed')

class usrRigister(CreateAPIView):
    """
    for user registeration
    """
    model = User
    serializer_class = UserSerializer

class ResetPass(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,) 

    def post(self, request, format=None):
        if request.user.is_authenticated():
            user = request.user
            npass = request.data['npass']
            opass = request.data['opass']
            if npass and user.check_password(opass):
                user.set_password(npass)
                user.save()
                return Response(user.username, status=status.HTTP_202_ACCEPTED)
            print(npass, user.check_password(opass))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def repeat_user(request):
    if request.method == 'GET':
        uname = request.query_params.get('username', None)
        if uname and not User.objects.filter(username=uname).exists():
            return Response('pass')
        else:
            return Response('denied')
    return Response('wrong method', status = status.HTTP_400_BAD_REQUEST)  
