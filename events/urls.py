from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='home'),
    path('by_type/', views.by_type, name='by_type'),
    path('login/', views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("createEvent/", views.create_event, name="create"),
    path("event/<str:pk>/", views.event, name='event'),
    path("your/<str:pk>/", views.your, name='your'),


]