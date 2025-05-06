from django.urls import path
from Yieldapp import views

app_name = 'yieldapp'
urlpatterns = [
    path('harvest/', views.index, name='index'),
]
