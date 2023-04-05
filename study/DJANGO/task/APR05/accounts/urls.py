
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('mypage/<int:pk>', views.mypage, name='mypage'),
] 
