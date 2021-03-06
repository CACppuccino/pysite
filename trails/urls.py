from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
from trails import views as tviews

urlpatterns = [

	url(r'^person/bags/$',tviews.bags),
	url(r'^person/download/$',tviews.downloads),
	url(r'^usr/logout/$',tviews.log_user_out),
	url(r'^usr/register/$', tviews.user_register, name = 'register'),
	url(r'^usr/dashboard/$',tviews.dashboard, name= 'dash_board'),
	url(r'^con/$',tviews.contri_index, name = 'con_index'),
	url(r'^con/(?P<sid>.*)$', tviews.contri_doc, name = 'con_doc'),
	url(r'^lstreet/$',tviews.lost_street_index, name = 'lstreet_index')
]


