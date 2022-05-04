from django.template.defaulttags import url
from django.urls import path
from django.contrib.auth.views import auth_login

from pinterest import views
from pinterest.views import *

urlpatterns = [
    path('', index),
    path('login.html', views.login, name='login'),
    path('registration.html', views.register, name='register'),
    path('cabinet.html', cabinet),
    path('logout', views.logout, name='logout'),


    # \path('pin/<int:id>/', get_pin_by_id, name="pin_id")

]
