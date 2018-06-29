from django.conf.urls import url, include
from . import views

app_name = 'street'

urlpatterns = [
    url(r'^api_index_page/', views.index_page.as_view()),
    url(r'^api_street_page/', views.street_page.as_view()),
    url(r'^api_street_comment/', views.street_comment.as_view()),
]
