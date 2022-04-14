from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('create.html', views.image_create, name='image_create'),
]
