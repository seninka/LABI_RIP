"""lab6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bdwork.views import *


urlpatterns = [
    url(r'^1/', basicone),
    url(r'^2/', Users.as_view()),
    url(r'^users/get/(?P<user_id>\d+)/$', singleuser),
    url(r'^"/users/addserves/(?P<user_id>\d+)/$', addserves),
    url(r'^users/all/$', users),
    url(r'^', users),
]
