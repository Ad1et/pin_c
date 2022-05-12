from django.template.defaulttags import url
from django.urls import path
from django.contrib.auth.views import auth_login

from pinterest import views
from pinterest.views import *

app_name = 'pinterest'
urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
]
