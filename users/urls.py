from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration ,name='user-registration'),
    path('profile/', views.profile ,name='profile')
]
