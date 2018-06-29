from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token 
from . import views

app_name = 'uinfo'

urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token), # alternative built in api in restframework-jwt, now using this 
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^usrRegister/$', views.usrRigister.as_view()),
    url(r'^basicInfo/$', views.UserList.as_view()),
    url(r'^authValidate/$', views.usrValidate.as_view()),
    url(r'repeatUser/$', views.repeat_user)
]

