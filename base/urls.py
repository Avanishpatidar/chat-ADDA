from django.urls import path
from . import views

urlpatterns = [
    #path('login/', views.loginPage, name="login"),
    #path('logout/', views.logoutUser, name="logout"),
    #path('register/', views.registerPage, name="register"),
    path('home', views.home, name="home"),
    #path('', views.home, name="home"),
   # path('room/<str:pk>/', views.room, name="room"),
]