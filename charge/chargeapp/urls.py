from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^maps/', views.maps, name ='maps'),
	url(r'^list/$', views.list, name='list'),
	url(r'^filterCOVList/$', views.filterCOVList, name='filterCOVList'),
	url(r'^create-user/$', views.create_user, name='create_user'),
	url(r'^login/$', views.login, name='login'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^delete/$', views.delete, name='delete'),
	url(r'^new-charging-station/$', views.new_charging_station, name='new_charging_station'),
	url(r'^use-charging-station/$', views.use_charging_station, name='use_charging_station'),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url('', include('django.contrib.auth.urls', namespace='auth')),
	url(r'^twitter/$', views.twitter, name='twitter'),
	url(r'^twitter/posttw/$', views.posttw, name='posttw'),
	url(r'^twitter/posttw/sharetw$', views.sharetw, name='sharetw'),
	url(r'^facebook/$', views.facebook, name='facebook'),
	url(r'^facebook/postfb/$', views.postfb, name='postfb'),
	url(r'^facebook/postfb/sharefb$', views.sharefb, name='sharefb'),
    url(r'^logoutuser/$', views.logoutuser, name='logout'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^privacy/$', views.privacy, name='privacy'),

]

