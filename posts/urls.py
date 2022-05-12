from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('create/', views.create_pin, name='create_pin'),
    path('edit/<int:id>', views.edit_pin, name='edit_pin'),
    path('delete/<int:id>', views.delete_pin, name='delete_pin'),
    path('comment/<int:id>', views.add_comment, name='add_comment'),
    path('delete-comment/<int:id>', views.delete_comment, name='delete_comment'),
    path('pin/<int:id>/', views.pin_detail, name='pin_detail'),
    path('<str:username>/created/', views.created_pins, name='created_pins'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

