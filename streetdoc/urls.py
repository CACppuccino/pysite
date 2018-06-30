from django.conf.urls import url, include
from . import views

app_name = 'streetdoc'

urlpatterns = [
    url(r'^api_street_list/', views.StreetList.as_view()),
    url(r'^api_street_info/', views.StreetInfo.as_view()),
]
