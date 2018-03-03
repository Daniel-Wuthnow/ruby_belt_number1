from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^login$', views.login),
	url(r'^register$', views.register),
	url(r'^home$', views.home),
	url(r'^logout$', views.logout),
	url(r'^wish_items/create$', views.add),
	url(r'^add$', views.create),
	url(r'^wish_items/(?P<number>\d+)$', views.show),
	url(r'^delete/(?P<number>\d+)$', views.destroy),
	url(r'^join/(?P<number>\d+)$', views.join),
	url(r'^remove/(?P<number>\d+)$', views.remove),
]