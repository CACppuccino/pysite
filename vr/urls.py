from django.conf.urls import url, include
from . import views

app_name = 'vr'

urlpatterns = [
    url(r'^api_download_page', views.version),
]
