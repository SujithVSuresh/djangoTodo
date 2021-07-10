from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('register/', views.register, name="register"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
]