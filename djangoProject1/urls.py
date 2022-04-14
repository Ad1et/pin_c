from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pinterest.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace='posts')),

]
