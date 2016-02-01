from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^maps/', views.maps, name ='maps'),
	url(r'^list/$', views.list, name='list'),
	url(r'^create-user/$', views.create_user, name='create_user'),
	url(r'^login/$', views.login, name='login'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^delete/$', views.delete, name='delete'),
	url(r'^new-charging-station/$', views.new_charging_station, name='new_charging_station'),
	url(r'^use-charging-station/$', views.use_charging_station, name='use_charging_station'),
    url(r'^logout/$', views.logout_view, name='logout'),
]

