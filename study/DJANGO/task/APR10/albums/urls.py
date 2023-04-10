from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('',views.album, name='album'),
    path('create/',views.create, name='create'),
]
