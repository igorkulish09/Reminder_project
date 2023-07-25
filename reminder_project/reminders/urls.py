from django.urls import path
from . import views

app_name = 'reminders'

urlpatterns = [
    path('', views.create_reminder, name='create-reminder'),
    path('create/', views.create_reminder, name='create_reminder'),
    path('<int:pk>/', views.reminders_detail, name='reminder_detail'),
]
