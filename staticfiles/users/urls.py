from django.urls import path
from . import views

urlpatterns = [
    path('add-user', views.addUser, name='addUser'),
    path('users-grid', views.usersGrid, name='usersGrid'),
    path('users-list', views.usersList, name='usersList'),
    path('view-profile', views.viewProfile, name='viewProfile'),
    path('login/', views.login, name='login'),
]