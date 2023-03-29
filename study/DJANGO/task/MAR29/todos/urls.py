
from django.urls import path
from . import views

app_name='todos'
urlpatterns = [
    path('', views.todo, name = 'todo'),
    path('<int:pk>/', views.todocontent, name = 'todocontent'),
    path('create/', views.create, name = 'create'),
    path('success/', views.success, name = 'success'),
    path('<int:pk>/remove', views.remove, name = 'remove'),
    path('<int:pk>/edit', views.edit, name = 'edit'),
    path('<int:pk>/update', views.update, name = 'update'),
]
