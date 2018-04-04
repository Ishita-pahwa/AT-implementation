from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	PostDetailView,
	start_page,
	link,
	donate,
	contact
	)

urlpatterns = [
	url(r'^home/$', start_page,name='home'),
	url(r'^link/$', link,name='link'),
	url(r'^donate/$', donate,name='donate'),
	url(r'^contact/$', contact,name='contact'),
	url(r'^blogs/$', post_list, name='list'),
    url(r'^create/$', post_create),
    #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail'), #Django Code Review #3 on joincfe.com/youtube/
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
