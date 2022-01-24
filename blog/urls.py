from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('base/', views.base, name='blog-base'),
]
