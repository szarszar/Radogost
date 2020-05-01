from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='home'),
    path('new/', views.new, name='new'),
    path('login/', views.loginPage, name="login"),
    path("home/", views.home,),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("createEvent/", views.CreateEvent, name="create"),
    path("event/<str:pk>", views.event, name='event'),


]