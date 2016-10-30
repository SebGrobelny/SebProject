from django.conf.urls import url
from django.contrib import admin


from .views import  posts_create, posts_delete, posts_list, posts_detail, posts_update



urlpatterns = [
	url(r'^create/$', posts_create, name = 'posts_create'),
	url(r'^(?P<id>\d+)/delete/$', posts_delete, name = 'posts_delete'),
	url(r'^$', posts_list, name = 'list'),
	url(r'^(?P<id>\d+)/$', posts_detail, name = 'detail'),
	url(r'^(?P<id>\d+)/update/$', posts_update, name = 'posts_update')


	]