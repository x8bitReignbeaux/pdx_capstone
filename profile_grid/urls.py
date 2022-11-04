from django.urls import path
from . import views

app_name = 'profile_grid'

urlpatterns = [
    path('', views.profile_grid, name='profile_grid'),
    path('user-profile', views.profile, name='profile'),
]