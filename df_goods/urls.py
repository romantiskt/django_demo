from django.conf.urls import url

from df_goods import views

urlpatterns = [
    url(r'^index$', views.index),
]
