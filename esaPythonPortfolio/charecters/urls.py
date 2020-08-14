from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_charecters, name='display_charecters'),
    path('create_charecter/', views.create_charecter, name='create_charecter'),
    path('update_charecter/<str:pk>/',
         views.update_charecter, name='update_charecter'),
    path('delete_charecter/<str:pk>/',
         views.delete_charecter, name='delete_charecter'),
    path('success/', views.success, name='success'),
    path('display_teams/', views.display_teams, name='display_teams'),
    path('create_team/', views.create_team, name='create_team'),
    path('update_team/<str:pk>/',
         views.update_team, name='update_team'),
    path('delete_team/<str:pk>/',
         views.delete_team, name='delete_team'),
]
app_name = "charecters"
