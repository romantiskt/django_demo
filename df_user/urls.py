from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handler/$', views.register_handler),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login/$', views.login),
    url(r'^login_handler$', views.login_handler),
    url(r'^info$', views.user_info),
    url(r'^site$', views.user_site),
]
