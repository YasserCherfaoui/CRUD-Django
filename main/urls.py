from django.urls import path
from .views import index, read, create, delete, update
app_name = 'main'


urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('update/<int:post_id>', update, name='update'),
    path('read/<int:post_id>', read, name='read'),
    path('delete/<int:post_id>', delete, name='delete'),
]
