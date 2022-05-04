from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('create.html', views.image_create, name='image_create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

