from django.urls import path
from . import views

app_name = 'qnapp'

urlpatterns = [
    path('questions/', views.question_list, name='question_list'),
    path('ask/', views.ask_question, name='ask_question'),
    # Add more URLs as needed
]
