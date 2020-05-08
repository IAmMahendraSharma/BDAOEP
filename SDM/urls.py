from django.urls import path
from . import views

urlpatterns = [
    ### SDM urls ###
    path('', views.index, name="Index"),
    path('add/', views.add, name="AddStudent"),
    path('logout/', views.logout, name="Logout"),
    path('login/', views.index, name="LoginForm"),
    path('login1/', views.login1, name="LoginData"),
    path('update/', views.update, name="UpdateStudent"),
    path('delete/', views.delete, name="DeleteStudent"),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('register/', views.register, name="RegisterForm"),
    path('register1/', views.register1, name="RegisterData"),
]
