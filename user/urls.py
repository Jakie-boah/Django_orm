from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.update_profile, name='profile'),
]
