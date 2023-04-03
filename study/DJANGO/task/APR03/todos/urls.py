from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'todos'
urlpatterns = [
    path('', views.todo, name='todo'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)