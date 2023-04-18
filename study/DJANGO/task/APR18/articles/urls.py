
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/likes/', views.likes, name='likes'),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:pk>/comments/<int:comment_pk>/likes/', views.comment_likes, name='comment_likes'),
    path('<int:pk>/emotes/<int:emotion>/', views.emotes, name='emotes'),
]

