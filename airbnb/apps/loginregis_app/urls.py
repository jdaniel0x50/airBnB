from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^$', views.index, name="login_index"),
    url(r'^register/$', views.register, name="register"),
    url(r'^success/$', views.success, name="success"),
    url(r'^process/$', views.process, name="process"),
    url(r'^logging/$', views.main_login, name="main_login"),
    url(r'^clear/$', views.clear, name="clear")
]