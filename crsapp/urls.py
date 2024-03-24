from django.urls import path
from . import views  # Assuming your views are in the same directory

urlpatterns = [
  path('', views.home, name='home'),
  path('result/', views.result, name='result'),
]