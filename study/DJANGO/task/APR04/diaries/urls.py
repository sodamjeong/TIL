
from django.urls import path
from . import views

app_name = 'diaries'
urlpatterns = [
    path('', views.diary, name='diary'),
    path('<int:pk>/', views.diarypage, name='diarypage'),
    path('write/', views.write, name='write'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),
]
