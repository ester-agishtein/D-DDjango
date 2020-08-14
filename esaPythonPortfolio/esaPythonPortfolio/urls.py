from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dndDice/', include('dndDice.urls', namespace="dndDice")),
    path('charecters/', include('charecters.urls', namespace="charecters"), name="charecters"),
    path('admin/', admin.site.urls),
]
