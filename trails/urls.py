from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
from trails import views as tviews

urlpatterns = [
	url(r'^person/(?P<numm>[0-9])/$',tviews.checkperson),
	url(r'^person/bags/$',tviews.bags),
	url(r'^person/download/$',tviews.downloads),
	url(r'^usr/logout/$',tviews.log_user_out),
	url(r'^usr/dashboard/$',tviews.dashboard),
]


