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
    path('create_team/', views.create_team, name='create_team'),
]
app_name = "charecters"
