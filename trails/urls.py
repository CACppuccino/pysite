from django.conf.urls import url
#from rest_framework.urlpatterns import format_suffix_patterns
from trails import views as tviews

urlpatterns = [
	url(r'^person/(?P<numm>[0-9])/$',tviews.checkperson),
	url(r'^person/bags/$',tviews.bags)
]

